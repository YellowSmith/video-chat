import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.set_todos(todos)

st.title("My first web app on python")
st.subheader("Todos web app aftermath")
st.write("Some simple text")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")