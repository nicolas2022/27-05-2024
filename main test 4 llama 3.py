import customtkinter as ctk

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure_interface()

    def configure_interface(self):
        self.tab_manager = ctk.CTkTabview(self, width=800, height=600)
        self.tab_manager.pack(fill="both", expand=True)

        self.onglet1 = self.tab_manager.add("Enregistrement ADD")
        self.onglet2 = self.tab_manager.add("Sélection de dossier")
        self.onglet3 = self.tab_manager.add("Suivi de dossier")
        self.onglet4 = self.tab_manager.add("Extraction")

        self.configure_onglet1()

    def configure_onglet1(self):
        self.onglet1.configure(fg_color="#333")
        self.create_onglet1_ligne1()
        self.create_onglet1_ligne2()
        self.create_onglet1_ligne3()
        self.create_onglet1_ligne4()
        self.create_onglet1_ligne5()
        self.create_onglet1_ligne6()
        self.create_onglet1_ligne7()
        self.create_onglet1_ligne8()

    def create_onglet1_ligne1(self):
        self.onglet1ligne1 = ctk.CTkLabel(self.onglet1, text="DEMANDEUR", font=("Arial", 14, "bold"), fg_color="#333", text_color="white")
        self.onglet1ligne1.pack(fill="x", pady=10)

    def create_onglet1_ligne2(self):
        self.onglet1ligne2 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne2.pack(anchor="center", pady=5)

        self.onglet1ligne2_1 = ctk.CTkComboBox(self.onglet1ligne2, width=170, values=["Association", "Bailleur social", "CCAS", "Centre médico-social", "Département", "Maison de métropole", "Maison du Rhône", "Autre"], command=self.update_case, state="readonly")
        self.onglet1ligne2_1.pack(side="left", padx=10)
        self.onglet1ligne2_1.bind("<<ComboboxSelected>>", self.update_case)
        self.onglet1ligne2_1.bind("<Button-1>", self.open_combobox)
        self.onglet1ligne2_1.bind("<Return>", self.check_selection)

        self.onglet1ligne2_2 = ctk.CTkLabel(self.onglet1ligne2, text="Nom si association", fg_color="#333", text_color="white")
        self.onglet1ligne2_2.pack(side="left", padx=10)

        self.onglet1ligne2_3 = ctk.CTkEntry(self.onglet1ligne2, width=326, fg_color="#333", text_color="white")
        self.onglet1ligne2_3.pack(side="left", padx=10)
        self.onglet1ligne2_3.bind("<Return>", self.focus_next_entry)

    def create_onglet1_ligne3(self):
        self.onglet1ligne3 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne3.pack(anchor="center", pady=5)

        self.onglet1ligne3_1 = ctk.CTkLabel(self.onglet1ligne3, text="Adresse", fg_color="#333", text_color="white")
        self.onglet1ligne3_1.pack(side="left", padx=10)

        self.onglet1ligne3_2 = ctk.CTkEntry(self.onglet1ligne3, width=579, fg_color="#333", text_color="white")
        self.onglet1ligne3_2.pack(side="left", padx=10)
        self.onglet1ligne3_2.bind("<Return>", self.focus_next_entry)

    def create_onglet1_ligne4(self):
        self.onglet1ligne4 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne4.pack(anchor="center", pady=5)

        self.onglet1ligne4_1 = ctk.CTkLabel(self.onglet1ligne4, text="Code postal", fg_color="#333", text_color="white")
        self.onglet1ligne4_1.pack(side="left", padx=10)

        self.onglet1ligne4_2 = ctk.CTkEntry(self.onglet1ligne4, width=50, fg_color="#333", text_color="white")
        self.onglet1ligne4_2.pack(side="left", padx=10)
        self.onglet1ligne4_2.bind("<KeyRelease>", self.limit_character_count)
        self.onglet1ligne4_2.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne4_3 = ctk.CTkLabel(self.onglet1ligne4, text="Ville", fg_color="#333", text_color="white")
        self.onglet1ligne4_3.pack(side="left", padx=10)

        self.onglet1ligne4_4 = ctk.CTkEntry(self.onglet1ligne4, width=192, fg_color="#333", text_color="white")
        self.onglet1ligne4_4.pack(side="left", padx=10)
        self.onglet1ligne4_4.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne4_5 = ctk.CTkLabel(self.onglet1ligne4, text=" ", fg_color="#333", text_color="#333", width=232)
        self.onglet1ligne4_5.pack(side="left", padx=10)

    def update_case(self, event=None):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.configure(state="normal", fg_color="#333")
        else:
            self.onglet1ligne2_3.delete(0, 'end')
            self.onglet1ligne2_3.configure(state="disabled", fg_color="black")

    def open_combobox(self, event):
        self.onglet1ligne2_1.tk_focusPrev().focus()
        event.widget.focus()
        event.widget.event_generate('<Down>')

    def check_selection(self, event):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.focus()
        else:
            self.onglet1ligne3_2.focus()

    def limit_character_count(self, event):
        widget = event.widget
        if len(widget.get()) > 5:
            widget.delete(5, 'end')

    def focus_next_entry(self, event):
        event.widget.tk_focusNext().focus()

    def create_onglet1_ligne5(self):
        self.onglet1ligne5 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne5.pack(anchor="center", pady=5)

        self.onglet1ligne5_1 = ctk.CTkLabel(self.onglet1ligne5, text="Référent(e) :", fg_color="#333", text_color="white")
        self.onglet1ligne5_1.pack(side="left", padx=10)

        self.onglet1ligne5_2 = ctk.CTkComboBox(self.onglet1ligne5, width=70, values=[" ", "M.", "Mme"], state="readonly")
        self.onglet1ligne5_2.pack(side="left", padx=10)
        self.onglet1ligne5_2.bind("<Button-1>", self.open_combobox)

        self.onglet1ligne5_3 = ctk.CTkLabel(self.onglet1ligne5, text="Nom", fg_color="#333", text_color="white")
        self.onglet1ligne5_3.pack(side="left", padx=10)

        self.onglet1ligne5_4 = ctk.CTkEntry(self.onglet1ligne5, width=165, fg_color="#333", text_color="white")
        self.onglet1ligne5_4.pack(side="left", padx=10)
        self.onglet1ligne5_4.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne5_5 = ctk.CTkLabel(self.onglet1ligne5, text="Prénom", fg_color="#333", text_color="white")
        self.onglet1ligne5_5.pack(side="left", padx=10)

        self.onglet1ligne5_6 = ctk.CTkEntry(self.onglet1ligne5, width=165, fg_color="#333", text_color="white")
        self.onglet1ligne5_6.pack(side="left", padx=10)
        self.onglet1ligne5_6.bind("<Return>", self.focus_next_entry)

    def create_onglet1_ligne6(self):
        self.onglet1ligne6 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne6.pack(anchor="center", pady=5)

        self.onglet1ligne6_1 = ctk.CTkLabel(self.onglet1ligne6, text="Téléphone 1", fg_color="#333", text_color="white")
        self.onglet1ligne6_1.pack(side="left", padx=10)

        self.onglet1ligne6_2 = ctk.CTkEntry(self.onglet1ligne6, width=90, fg_color="#333", text_color="white")
        self.onglet1ligne6_2.pack(side="left", padx=10)
        self.onglet1ligne6_2.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne6_3 = ctk.CTkLabel(self.onglet1ligne6, text="Téléphone 2", fg_color="#333", text_color="white")
        self.onglet1ligne6_3.pack(side="left", padx=10)

        self.onglet1ligne6_4 = ctk.CTkEntry(self.onglet1ligne6, width=90, fg_color="#333", text_color="white")
        self.onglet1ligne6_4.pack(side="left", padx=10)
        self.onglet1ligne6_4.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne6_5 = ctk.CTkLabel(self.onglet1ligne6, text=" ", fg_color="#333", text_color="#333", width=243)
        self.onglet1ligne6_5.pack(side="left", padx=10)

    def create_onglet1_ligne7(self):
        self.onglet1ligne7 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne7.pack(anchor="center", pady=5)

        self.onglet1ligne7_1 = ctk.CTkLabel(self.onglet1ligne7, text="Mail", fg_color="#333", text_color="white")
        self.onglet1ligne7_1.pack(side="left", padx=10)

        self.onglet1ligne7_2 = ctk.CTkEntry(self.onglet1ligne7, width=350, fg_color="#333", text_color="white")
        self.onglet1ligne7_2.pack(side="left", padx=10)
        self.onglet1ligne7_2.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne7_3 = ctk.CTkLabel(self.onglet1ligne7, text=" ", fg_color="#333", text_color="#333", width=230)
        self.onglet1ligne7_3.pack(side="left", padx=10)

    def create_onglet1_ligne8(self):
        self.onglet1ligne8 = ctk.CTkFrame(self.onglet1, fg_color="#333")
        self.onglet1ligne8.pack(anchor="center", pady=5)

        self.onglet1ligne8_1 = ctk.CTkLabel(self.onglet1ligne8, text="Mail en copie", fg_color="#333", text_color="white")
        self.onglet1ligne8_1.pack(side="left", padx=10)

        self.onglet1ligne8_2 = ctk.CTkEntry(self.onglet1ligne8, width=350, fg_color="#333", text_color="white")
        self.onglet1ligne8_2.pack(side="left", padx=10)
        self.onglet1ligne8_2.bind("<Return>", self.focus_next_entry)

        self.onglet1ligne8_3 = ctk.CTkLabel(self.onglet1ligne8, text=" ", fg_color="#333", text_color="#333", width=180)
        self.onglet1ligne8_3.pack(side="left", padx=10)

    def update_case(self, event=None):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.configure(state="normal", fg_color="#333")
        else:
            self.onglet1ligne2_3.delete(0, 'end')
            self.onglet1ligne2_3.configure(state="disabled", fg_color="black")

    def open_combobox(self, event):
        # Fermer toutes les autres fenêtres de combobox ouvertes
        self.onglet1ligne2_1.tk_focusPrev().focus()
        event.widget.focus()
        event.widget.event_generate('<Down>')

    def check_selection(self, event):
        if self.onglet1ligne2_1.get() == "Association":
            self.onglet1ligne2_3.focus()
        else:
            self.onglet1ligne3_2.focus()

    def limit_character_count(self, event):
        widget = event.widget
        if len(widget.get()) > 5:
            widget.delete(5, 'end')

    def focus_next_entry(self, event):
        event.widget.tk_focusNext().focus()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
