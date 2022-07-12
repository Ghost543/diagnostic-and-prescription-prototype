import tkinter as tk
import customtkinter

import bot
import prescription_logic

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class GUI(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520


    def __init__(self):
        super().__init__()
        self.windowWidth = self.winfo_reqwidth()
        self.windowHeight = self.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        self.positionRight = int(self.winfo_screenwidth() / 2 - GUI.WIDTH / 2)
        self.positionDown = int(self.winfo_screenheight() / 2 - GUI.HEIGHT / 2)

        self.title("Diseases Diagnostic")
        self.geometry(f"{GUI.WIDTH}x{GUI.HEIGHT}+{self.positionRight}+{self.positionDown}")
        self.minsize(GUI.WIDTH, GUI.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Control Variables
        self.entry_var = tk.StringVar()

        self.symptoms = list()

        frame_1_w = GUI.WIDTH * 0.9
        self.frame = customtkinter.CTkFrame(master=self, width=frame_1_w)
        self.frame.grid(row=0, column=1, sticky="nswe", padx=40, pady=40)

        # frame.rowconfigure((0, 1, 2, 3), weight=1)
        # frame.rowconfigure(7, weight=10)
        self.frame.columnconfigure((0, 1), weight=10)
        self.frame.columnconfigure(4, weight=10)

        self.frame_symptom = customtkinter.CTkFrame(master=self.frame)
        self.frame_symptom.grid(row=1, column=1, columnspan=2, rowspan=5, pady=20, padx=20, sticky="nsew")

        self.frame_symptom.columnconfigure(0, weight=1)
        self.frame_symptom.columnconfigure(4, weight=1)

        self.entry = customtkinter.CTkEntry(master=self.frame, width=120, textvariable=self.entry_var,
                                            placeholder_text='Enter symptom and press "Add symptom"')
        self.entry.grid(row=0, column=1, columnspan=2, pady=20, padx=20, sticky="we")

        self.symptom_label = None

        self.button = customtkinter.CTkButton(master=self.frame, text="Add symptom", command=self.add_symptom)
        self.button.grid(row=0, column=3, pady=20, padx=20, sticky="we")

        self.diagnose_btn = customtkinter.CTkButton(master=self.frame, text="Diagnose", command=self.diagnose)
        self.diagnose_btn.grid(row=8, column=3, padx=20, pady=20, sticky="we")

        if len(self.symptoms) <= 0:
            self.diagnose_btn.configure(state=tk.DISABLED)
        else:
            self.diagnose_btn.configure(state=tk.ACTIVE)

    def add_symptom(self):
        if self.entry_var.get():
            position = len(self.symptoms)
            column = 1
            if len(self.symptoms) >= 4:
                column = 2
                position = len(self.symptoms) - 4
            interpreted_symp = bot.get_response(self.entry_var.get())
            print(interpreted_symp)
            self.symptoms.append(interpreted_symp)
            self.symptom_label = customtkinter.CTkLabel(master=self.frame_symptom,
                                                        text=interpreted_symp,
                                                        height=20,
                                                        fg_color=("white", "gray38"),  # <- custom tuple-color
                                                        justify=tk.LEFT)
            self.symptom_label.grid(column=column, row=position, sticky="nwe", padx=15, pady=10)
            self.entry_var.set("")
            self.diagnose_btn.configure(state=tk.ACTIVE)

    def diagnose(self):
        print(self.symptoms)
        window = customtkinter.CTkToplevel(self)
        width = 800
        height = 600

        positionRight = int(self.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.winfo_screenheight() / 2 - height / 2)

        window.geometry(f"{width}x{height}+{positionRight}+{positionDown}")
        window.minsize(GUI.WIDTH, GUI.HEIGHT)
        window.title("Prescription for Diagnosed Diseases")

        window.rowconfigure(4, weight=40)
        window.columnconfigure((0, 1), weight=10)
        window.columnconfigure(4, weight=10)
        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(master=window,
                                       text="Possible Diagnosis",
                                       height=40,
                                       fg_color=("white", "gray20"),
                                       text_font=("Roboto Medium", 18),  # <- custom tuple-color
                                       justify=tk.LEFT)
        label.grid(row=1, column=0, columnspan=1, pady=40, padx=40, sticky="nsew")

        lkhd_1 = customtkinter.CTkFrame(master=window)
        lkhd_1.grid(row=2, column=0, columnspan=2, padx=40, sticky="nsew", ipady=10)

        # lkhd_1.columnconfigure(0, weight=1)
        lkhd_1.columnconfigure(4, weight=1)

        lkhd_2 = customtkinter.CTkFrame(master=window)
        lkhd_2.grid(row=3, column=0, columnspan=2, pady=20, padx=40, sticky="nsew", ipady=10)

        # lkhd_2.columnconfigure(0, weight=1)
        lkhd_2.columnconfigure(4, weight=1)

        d_label_1 = customtkinter.CTkLabel(master=lkhd_1,
                                           text="Disease 1",
                                           height=40,
                                           width=40,
                                           fg_color=("white", "#2EB086"),
                                           text_font=("Roboto Medium", 14),  # <- custom tuple-color
                                           corner_radius=35)
        d_label_1.grid(row=0, column=0, padx=30, pady=10, sticky="nwe")

        p_label_1 = customtkinter.CTkLabel(master=lkhd_1,
                                           text="86%",
                                           height=10,
                                           width=60,
                                           fg_color=("white", "#F76E11"),
                                           text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                           corner_radius=5)
        p_label_1.grid(row=0, column=1, pady=20, sticky="nwe")

        def prescribe1():
            inner_frame = customtkinter.CTkFrame(master=lkhd_1, fg_color=("white", "gray26"))
            inner_frame.grid(row=1, column=2, columnspan=3)
            prescription1 = customtkinter.CTkLabel(master=inner_frame,
                                                   text="prescription 1 (2x3)",
                                                   height=15,
                                                   width=15,
                                                   fg_color=("white", "#9C0F48"),
                                                   text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                                   corner_radius=15)
            prescription1.grid(row=1, column=1, pady=10, padx=10, ipady=10)
            prescription2 = customtkinter.CTkLabel(master=inner_frame,
                                                   text="prescription 2 (1x2)",
                                                   height=15,
                                                   width=15,
                                                   fg_color=("white", "#9C0F48"),
                                                   text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                                   corner_radius=15)
            prescription2.grid(row=2, column=1, pady=10, padx=10, ipady=10)

        btn_1 = customtkinter.CTkButton(master=lkhd_1,
                                        text="Prescribe",
                                        width=50,
                                        height=10,
                                        border_width=3,
                                        border_color="#9C0F48",
                                        corner_radius=20,
                                        fg_color=("gray84", "gray25"),
                                        hover_color="#9C0F48",
                                        command=prescribe1)
        btn_1.grid(row=0, column=2, sticky="nwe", pady=21, padx=50)

        def prescribe2():
            inner_frame = customtkinter.CTkFrame(master=lkhd_2)
            inner_frame.grid(row=1, column=2, columnspan=3)
            prescription1 = customtkinter.CTkLabel(master=inner_frame,
                                                   text="prescription 1 (3x3)",
                                                   height=15,
                                                   width=15,
                                                   fg_color=("white", "#9C0F48"),
                                                   text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                                   corner_radius=15)
            prescription1.grid(row=1, column=1, pady=10, padx=10, ipady=10)
            prescription2 = customtkinter.CTkLabel(master=inner_frame,
                                                   text="prescription 2 (3x2)",
                                                   height=15,
                                                   width=15,
                                                   fg_color=("white", "#9C0F48"),
                                                   text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                                   corner_radius=15)
            prescription2.grid(row=2, column=1, pady=10, padx=10, ipady=10)

        d_label_2 = customtkinter.CTkLabel(master=lkhd_2,
                                           text="Disease 2",
                                           height=40,
                                           width=40,
                                           fg_color=("white", "#2EB086"),
                                           text_font=("Roboto Medium", 14),  # <- custom tuple-color
                                           corner_radius=35)
        d_label_2.grid(row=0, column=0, padx=30, pady=10, sticky="nwe")

        p_label_2 = customtkinter.CTkLabel(master=lkhd_2,
                                           text="11%",
                                           height=10,
                                           width=60,
                                           fg_color=("white", "#F76E11"),
                                           text_font=("Roboto Medium", 12),  # <- custom tuple-color
                                           corner_radius=5)
        p_label_2.grid(row=0, column=1, pady=20, sticky="nwe")

        btn_2 = customtkinter.CTkButton(master=lkhd_2,
                                        text="Prescribe",
                                        width=50,
                                        height=10,
                                        border_width=3,
                                        border_color="#9C0F48",
                                        corner_radius=20,
                                        fg_color=("gray84", "gray25"),
                                        hover_color="#9C0F48",
                                        command=prescribe2)
        btn_2.grid(row=0, column=2, sticky="nwe", pady=21, padx=50)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = GUI()
    app.start()
