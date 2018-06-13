def test():

    st = open("st.txt","w","encoding=utf=8")
    st.write("こんにちは from Python!")
    st.close()

if __name__ == "__main__":
    test()