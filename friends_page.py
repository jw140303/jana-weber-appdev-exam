import streamlit as st
from helpers import connect_to_deta, fetch_data

def friends_page():
    db_users = connect_to_deta('bookwish')
    db_user_friends = connect_to_deta(f'user-{st.session_state.user_name}-friends')

    user_data = fetch_data(db_users)
    user_names = list(user_data.user_name)

    user_friends_data = fetch_data(db_user_friends)
    user_friends = list(user_friends_data.friends)

    st.write('Your friends:')

    # giving the option to add a friend
    placeholder = st.empty()
    with placeholder.form('form'):
        new_friend = st.text_input('What to add a friend?:').lower()
        submitted = st.form_submit_button('Add friend 📖')
        close = st.form_submit_button('Close form ❌')

    if submitted:
        if new_friend in user_names:  # checking if the user exists
            if new_friend in user_friends:  # checking if the user is already in the friends list
                st.error('This person is already your friend!')
            else:
                db_user_friends.put({'friends': new_friend})  # adding the user to the friends list
                st.info('The user has been added to your friends!')
        elif new_friend == '':  # checking if the input is empty
            st.error('Please enter a user name!')
        else:
            st.error('This user does not exist! Please check your spelling or provide a different name')

    if close:
        placeholder.empty()

    #displaying the users friends-
    if user_friends == ['']:
        st.write('Looks like you have not added any friends yet!')
        st.write('To use this app to its full potential, you should consider adding some')
    else:
        for i in user_friends:
            st.write(f'- {i}')
            st.write('This is their wishlist:')
            db_i_wishlist = connect_to_deta(f'user-{i}-wishlist')
            i_wishlist = fetch_data(db_i_wishlist)
            st.dataframe(i_wishlist, use_container_width=True, column_order=("image", "book", "author"),
                         hide_index=True,
                         column_config={"image": st.column_config.ImageColumn()}
                         )
