import streamlit as st
books = [
  "The hobit",
  "1983",
  "The Great Gatsby",
  "To kill a Mockingbirf",
  "PRide and predjuce"
]
st.title("Book Checkmark")
st.write("Enter a book to check if it exists in the database")
user_input = st.text_input("Book Title")
if st.button("Check Book"):
  if user_input.strip() == "" :
    st.warning("Please enter a book")
elif user_input in books:
  st.success("The book you entered does exist in the database")
else:
  st.error("The book you entered is invalid and/or doesnt exist in our database")

         
