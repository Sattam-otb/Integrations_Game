import tkinter as tk
from tkinter import messagebox
import random

class MathGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("لعبة تكامل الدوال المثلثية")
        master.geometry("600x400")  # حجم النافذة الأولي
        master.config(bg="#f0f0f0")  # لون الخلفية الرئيسي

        self.قوانين_التكامل = {
            "∫ sin(x) dx": "-cos(x)",
            "∫ cos(x) dx": "sin(x)",
            "∫ sec^2(x) dx": "tan(x)",
            "∫ csc^2(x) dx": "-cot(x)",
            "∫ sec(x)tan(x) dx": "sec(x)",
            "∫ csc(x)cot(x) dx": "-csc(x)"
        }
        self.الدوال = list(self.قوانين_التكامل.keys())
        self.الإجابة_صحيحة = ""
        self.خيارات_إجابات = []
        self.السؤال_الحالي = ""
        self.النقاط = 0
        self.عدد_الأسئلة = 5
        self.سؤال_رقم = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.question_label.pack(pady=30)

        self.radio_buttons = []
        self.selected_answer = tk.StringVar()

        for i in range(4):
            radio_frame = tk.Frame(master, bg="#f0f0f0")
            radio_frame.pack(anchor=tk.W, padx=40, pady=5)
            radio_button = tk.Radiobutton(radio_frame, text="", variable=self.selected_answer, value="", font=("Arial", 14), bg="#e0e0e0", fg="#333", selectcolor="#a0a0a0")
            radio_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(master, text="تحقق من الإجابة", command=self.check_answer, font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.submit_button.pack(pady=30)

        self.score_label = tk.Label(master, text="النقاط: 0", font=("Arial", 14), bg="#f0f0f0", fg="#777")
        self.score_label.pack()

        self.next_question()

    def next_question(self):
        if self.سؤال_رقم < self.عدد_الأسئلة:
            self.السؤال_الحالي = random.choice(self.الدوال)
            self.الإجابة_صحيحة = self.قوانين_التكامل[self.السؤال_الحالي]

            self.خيارات_إجابات = [self.الإجابة_صحيحة]
            while len(self.خيارات_إجابات) < 4:
                إجابة_خاطئة = random.choice(list(self.قوانين_التكامل.values()))
                if إجابة_خاطئة not in self.خيارات_إجابات:
                    self.خيارات_إجابات.append(إجابة_خاطئة)
            random.shuffle(self.خيارات_إجابات)

            self.question_label.config(text=f"ما هو تكامل:\n{self.السؤال_الحالي}؟", justify="center")

            for i, خيار in enumerate(self.خيارات_إجابات):
                self.radio_buttons[i].config(text=f"{خيار} + C", value=خيار)
                self.selected_answer.set(self.خيارات_إجابات[0]) # اختيار افتراضي

            self.سؤال_رقم += 1
        else:
            messagebox.showinfo("انتهت اللعبة", f"حصلت على {self.النقاط} من {self.عدد_الأسئلة} إجابات صحيحة.")
            self.master.destroy()

    def check_answer(self):
        الإجابة_المختارة = self.selected_answer.get()
        if الإجابة_المختارة == self.الإجابة_صحيحة:
            messagebox.showinfo("نتيجة", "إجابة صحيحة! 👍")
            self.النقاط += 1
        else:
            messagebox.showerror("نتيجة", f"إجابة خاطئة.\nالإجابة الصحيحة هي:\n{self.الإجابة_صحيحة} + C")

        self.score_label.config(text=f"النقاط: {self.النقاط}")
        self.next_question()

root = tk.Tk()
game_gui = MathGameGUI(root)
root.mainloop()