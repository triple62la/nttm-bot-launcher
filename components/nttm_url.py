from tkinter import Entry, Label, Frame, Radiobutton, StringVar, Checkbutton, BooleanVar,SOLID


def init_nttm_url(root, saved_conf:dict):


    def other_input_toggle():
        if other_btn_isChecked.get():
            other_input.config(state="normal")
            other_input.focus_set()
            ttm_btn.config(state="disabled")
            vdi_btn.config(state="disabled")
        else:
            other_input.config(state="disabled")
            ttm_btn.config(state="normal")
            vdi_btn.config(state="normal")
            url.set('http://www.ttm.rt.ru')

    frame = Frame(root,borderwidth=1, relief=SOLID, pady=5, padx=5)
    Label(frame, text="Адрес NTTM:").grid(row=0, column=0)
    url = StringVar(frame, value=saved_conf.get("nttm_url", 'http://www.ttm.rt.ru'))
    url_lbl = Label(frame, textvariable=url)
    url_lbl.grid(row=0, column=1, columnspan=2)
    ttm_btn = Radiobutton(frame, text='ttm.rt.ru', value='http://www.ttm.rt.ru', variable=url)
    ttm_btn.grid(row=1, column=0)
    vdi_btn = Radiobutton(frame, text="VDI", value='http://192.168.68.56', variable=url)
    vdi_btn.grid(row=1, column=1)
    other_btn_isChecked = BooleanVar(frame, False)
    other_btn = Checkbutton(frame, text="Другое",variable=other_btn_isChecked,  command=other_input_toggle)
    other_btn.grid(row=1, column=2)
    other_input = Entry(frame, textvariable=url, state="disabled")
    other_input.grid(row=2, column=2, columnspan=3)
    return frame, url
