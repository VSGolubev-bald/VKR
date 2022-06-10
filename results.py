from tkinter import *
import psycopg2
import os

import results
import show


def view():
    conn = psycopg2.connect(host="localhost", database="envexp", user="postgres", password=os.getenv(pswd), port="1858")
    cur = conn.cursor()
    postgreSQL_select_Query = "select * from results where id = %s"

    cur.execute(postgreSQL_select_Query, (int(code_id.get()),))
    if(int(code_id.get()) == 0):
        show.CodeOne(results.filename)
    else:
        show.CodeTwo()
    conn.commit()

def submit():
    conn = psycopg2.connect(host="localhost", database="envexp", user="postgres", password=os.getenv(pswd), port="1858")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO devices(id, device_name, description)
    VALUES (%s, %s, %s);
    """,
                (int(res_id.get()), code_id.get(),filename.get()))
    conn.commit()
    conn.close

    device_id.delete(0, END)
    device_name.delete(0, END)
    descrp.delete(0, END)


def delete():
    conn = psycopg2.connect(host="localhost", database="envexp", user="postgres", password="Merida2009", port="1858")
    cur = conn.cursor()
    #cur.execute("DELETE FROM users WHERE id = %s", (2,))
    cur.execute("DELETE FROM devices WHERE id = %s;",  (int(delete_id.get()),))

    conn.commit()
    conn.close
    device_id.delete(0, END)




root = Tk()
root.title('results')
root.geometry("400x250")

#conn = psycopg2.connect(host="localhost", database="envexp", user="postgres", password="Merida2009", port="1858")

#c = conn.cursor()

res_id = Entry(root, width=30)
res_id.grid(row=0, column=1, padx=20)

code_id = Entry(root, width=30)
code_id.grid(row=1, column=1, padx=20)

filename = Entry(root, width=30)
filename.grid(row=2, column=1, padx=20)

delete_id = Entry(root, width=30)
delete_id.grid(row=4, column=1)

show_id = Entry(root, width=30)
show_id.grid(row=6, column=1)

res_id_label = Label(root, text="id")
res_id_label.grid(row=0, column=0)

code_id_label = Label(root, text="code_id")
code_id_label.grid(row=1, column=0)

filename_label = Label(root, text="filename")
filename_label.grid(row=2, column=0)

delete_label = Label(root, text="id")
delete_label.grid(row=4, column=0)

show_label = Label(root, text="id")
show_label.grid(row=6, column=0)

submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_btn = Button(root, text="Delete record from Database", command=delete)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

res_btn = Button(root, text="View results", command=view)
res_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
#conn.commit()
#conn.close
root.mainloop()

