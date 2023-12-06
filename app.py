import streamlit as st


def multiple_choice_survey():
    st.title("Find Your Christ")

    st.write("#### This survey is designed to help you visualize Jesus Christ in a new way")
    st.write("#### After answering 3 questions, you will be presented with an AI generated image of Christ")
    st.write("###### Note: These images were pre-generated using Bing Image Creator (Powered by DALLE-3) and are not perfect.")
    st.write("\n")
    st.write("\n")
    st.write("### Begin Survey:")

    selected_choice_1 = None
    selected_choice_2 = None
    selected_choice_3 = None

    # Question 1
    question_1 = "Would you rather visualize a picture about the nature of Jesus Christ or the life of Jesus Christ?"
    choices_1 = ["Nature of Jesus Christ", "Life of Jesus Christ"]
    selected_choice_1 = st.radio(question_1, choices_1, index=None)

    # Question 2
    if selected_choice_1 == "Nature of Jesus Christ":
        question_2 = "Select a sub category:"
        choices_2 = ["Divine", "Human"]
        selected_choice_2 = st.radio(question_2, choices_2, index=None)

    elif selected_choice_1 == "Life of Jesus Christ":
        question_2 = "Select a sub category:"
        choices_2 = ["Pre-Mortal", "Mortal", "Ministry", "Death", "Post-Mortal"]
        selected_choice_2 = st.radio(question_2, choices_2, index=None)
    else:
        st.write("Select answer above ^^")
        

    # Question 3
    if selected_choice_2 == "Divine":
        question_3 = "Final Selection:"
        choices_3 = ["Savior","Judge","Warrior","King"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Human":
        question_3 = "Select final attribute:"
        choices_3 = ["Prophet","Teacher","Healer","Friend"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Pre-Mortal":
        question_3 = "Select final attribute:"
        choices_3 = ["Creator","Son of God","Spirit"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Mortal":
        question_3 = "Select final attribute:"
        choices_3 = ["Birth","Studying","Carpenter"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Ministry":
        question_3 = "Select final attribute:"
        choices_3 = ["Miracles","Sacrament","Gethsemane"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Death":
        question_3 = "Select final attribute:"
        choices_3 = ["Crucifixion","Tomb","Resurrection"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)
    elif selected_choice_2 == "Post-Mortal":
        question_3 = "Select final attribute:"
        choices_3 = ["Appearances","Americas","Displaying Wounds","Ascended Christ"]
        selected_choice_3 = st.radio(question_3,choices_3, index=None)


    # Display Picture
    if selected_choice_3 == "Savior":
        st.image("Pictures\Christ as a Savior.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Judge":
        st.image("Pictures\Christ as a Judge.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Warrior":
        st.image("Pictures\Christ as a Warrior.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "King":
        st.image("Pictures\Christ as a King.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Prophet":
        st.image("Pictures\Christ as a Prophet.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Teacher":
        st.image("Pictures\Christ as a Teacher.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Healer":
        st.image("Pictures\Christ as a Healer.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Friend":
        st.image("Pictures\Christ as a Friend.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Creator":
        st.image("Pictures\Christ as Creator.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Son of God":
        st.image("Pictures\Christ as Son of God.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Spirit":
        st.image("Pictures\Christ as a Spirit.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Birth":
        st.image("Pictures\Christ Mortal Birth.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Studying":
        st.image("Pictures\Christ Studying.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Carpenter":
        st.image("Pictures\Christ as a Carpenter.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Miracles":
        st.image("Pictures\Christ as Miracle Worker.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Sacrament":
        st.image("Pictures\Christ with the Sacrament.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Gethsemane":
        st.image("Pictures\Christ in Gethsemane.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Crucifixion":
        st.image("Pictures\Christ on the Cross.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Tomb": 
        st.image("Pictures\Christ in Tomb.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Resurrection":
        st.image("Pictures\Christ Resurrected.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Appearances": 
        st.image("Pictures\Christ Appearing.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Americas":
        st.image("Pictures\Christ Visiting Americas.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Displaying Wounds":
        st.image("Pictures\Christ Displaying Wounds.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)
    elif selected_choice_3 == "Ascended Christ":
        st.image("Pictures\Christ as Ascended.jpg", caption=f"Picture for your selections: {selected_choice_1}, {selected_choice_2}, and {selected_choice_3}", use_column_width=True)


if __name__ == "__main__":
    multiple_choice_survey()
