import numpy as np
from dataclasses import dataclass
import dataclasses as dc


@dataclass(order=True)
class DenseLayer:
    neurons: any

    def relu(self, inputs):
        """
        ReLU Activation Function
        """
        return np.maximum(0, inputs)

    def softmax(self, inputs):
        """
        Softmax Activation Function
        """
        exp_scores = np.exp(inputs)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return probs

    def relu_derivative(self, dA, Z):
        """
        ReLU Derivative Function
        """
        dZ = np.array(dA, copy=True)
        dZ[Z <= 0] = 0
        return dZ

    def forward(self, inputs, weights, bias, activation):
        """
        Single Layer Forward Propagation
        """
        Z_curr = np.dot(inputs, weights.T) + bias

        if activation == 'relu':
            A_curr = self.relu(inputs=Z_curr)
        elif activation == 'softmax':
            A_curr = self.softmax(inputs=Z_curr)

        return A_curr, Z_curr

    def backward(self, dA_curr, W_curr, Z_curr, A_prev, activation):
        """
        Single Layer Backward Propagation
        """
        if activation == 'softmax':
            dW = np.dot(A_prev.T, dA_curr)
            db = np.sum(dA_curr, axis=0, keepdims=True)
            dA = np.dot(dA_curr, W_curr)
        else:
            dZ = self.relu_derivative(dA_curr, Z_curr)
            dW = np.dot(A_prev.T, dZ)
            db = np.sum(dZ, axis=0, keepdims=True)
            dA = np.dot(dZ, W_curr)

        return dA, dW, db


@dataclass(order=True)
class Network:
    network: list = dc.field(init=False, default_factory=list, repr=False)  ## layers
    architecture: list = dc.field(init=False, default_factory=list, repr=False)  ## mapping input neurons --> output neurons
    params: list = dc.field(init=False, default_factory=list, repr=False)  ## W, b
    memory: list = dc.field(init=False, default_factory=list, repr=False)  ## Z, A
    gradients: list = dc.field(init=False, default_factory=list, repr=False)  ## dW, db

    def add(self, layer):
        """
        Add layers to the network
        """
        self.network.append(layer)

    def _compile(self, data):
        """
    Initialize model architecture
    """
        for idx, layer in enumerate(self.network):
            if idx == 0:
                self.architecture.append({'input_dim': data.shape[1],
                                          'output_dim': self.network[idx].neurons,
                                          'activation': 'relu'})
            elif 0 < idx < len(self.network) - 1:
                self.architecture.append({'input_dim': self.network[idx - 1].neurons,
                                          'output_dim': self.network[idx].neurons,
                                          'activation': 'relu'})
            else:
                self.architecture.append({'input_dim': self.network[idx - 1].neurons,
                                          'output_dim': self.network[idx].neurons,
                                          'activation': 'softmax'})
        return self

    def _init_weights(self, data):
        """
        Initialize the model parameters
        """
        self._compile(data)

        np.random.seed(99)

        for i in range(len(self.architecture)):
            self.params.append({
                'W': np.random.uniform(low=-1, high=1,
                                       size=(self.architecture[i]['output_dim'],
                                             self.architecture[i]['input_dim'])),
                'b': np.zeros((1, self.architecture[i]['output_dim']))})

        return self

    def _forwardprop(self, data):
        """
        Performs one full forward pass through network
        """
        A_curr = data

        for i in range(len(self.params)):
            A_prev = A_curr
            A_curr, Z_curr = self.network[i].forward(inputs=A_prev,
                                                     weights=self.params[i]['W'],
                                                     bias=self.params[i]['b'],
                                                     activation=self.architecture[i]['activation'])

            self.memory.append({'inputs': A_prev, 'Z': Z_curr})

        return A_curr

    def _backprop(self, predicted, actual):
        """
        Performs one full backward pass through network
        """
        num_samples = len(actual)

        ## compute the gradient on predictions
        dscores = predicted
        dscores[range(num_samples), actual] -= 1
        dscores /= num_samples

        dA_prev = dscores

        for idx, layer in reversed(list(enumerate(self.network))):
            dA_curr = dA_prev

            A_prev = self.memory[idx]['inputs']
            Z_curr = self.memory[idx]['Z']
            W_curr = self.params[idx]['W']

            activation = self.architecture[idx]['activation']

            dA_prev, dW_curr, db_curr = layer.backward(dA_curr, W_curr, Z_curr, A_prev, activation)

            self.gradients.append({'dW': dW_curr, 'db': db_curr})

    def _update(self, lr=0.01):
        """
        Update the model parameters --> lr * gradient
        """
        for idx, layer in enumerate(self.network):
            self.params[idx]['W'] -= lr * list(reversed(self.gradients))[idx]['dW'].T
            self.params[idx]['b'] -= lr * list(reversed(self.gradients))[idx]['db']

    def _get_accuracy(self, predicted, actual):
        """
        Calculate accuracy after each iteration
        """
        return np.mean(np.argmax(predicted, axis=1) == actual)

    def _calculate_loss(self, predicted, actual):
        """
        Calculate cross-entropy loss after each iteration
        """
        samples = len(actual)

        correct_logprobs = -np.log(predicted[range(samples), actual])
        data_loss = np.sum(correct_logprobs) / samples

        return data_loss

    def train(self, X_train, y_train, epochs):
        """
        Train the model using SGD
        """
        self.loss = []
        self.accuracy = []

        self._init_weights(X_train)

        for i in range(epochs):
            yhat = self._forwardprop(X_train)
            self.accuracy.append(self._get_accuracy(predicted=yhat, actual=y_train))
            self.loss.append(self._calculate_loss(predicted=yhat, actual=y_train))

            self._backprop(predicted=yhat, actual=y_train)

            self._update()

            if i % 20 == 0:
                s = 'EPOCH: {}, ACCURACY: {}, LOSS: {}'.format(i, self.accuracy[-1], self.loss[-1])
                print(s)
