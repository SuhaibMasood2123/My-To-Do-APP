import streamlit as st
import app1_function

todos = app1_function.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    app1_function.set_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-Do APP")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        app1_function.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new to-do....", on_change=add_todo, key='new_todo')
