import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# --- Konfigurasi Persona Chatbot ---
BALI_GO_PERSONA = (
    "Anda adalah 'Bali Go', seorang asisten wisata ahli dan ramah untuk Pulau Bali. "
    "Tugas Anda adalah membantu pengguna merencanakan perjalanan mereka ke Bali. "
    "Gaya bahasa Anda harus santai, antusias, dan sangat informatif, menggunakan Bahasa Indonesia yang mudah dipahami. "
    "Berikan rekomendasi terbaik mengenai destinasi (pantai, pura, sawah), "
    "aktivitas, kuliner khas, dan tips perjalanan lokal (seperti etika berkunjung, transportasi, dan musim terbaik). "
    "Selalu bersikap profesional namun hangat."
)
# -----------------------------------

st.set_page_config(page_title="Bali Go", page_icon="🌴")
st.title("🌴 Bali Go - Asisten Wisata Anda")

def get_api_key_input():
    if "GOOGLE_API_KEY" not in st.session_state:
        st.session_state["GOOGLE_API_KEY"] = ""

    if st.session_state["GOOGLE_API_KEY"]:
        return

    st.markdown("### Masukkan Google API Key Anda")
    st.info("Kunci ini diperlukan untuk menjalankan model Gemini.")

    col1, col2 = st.columns((80, 20))
    with col1:
        api_key = st.text_input("API Key", label_visibility="collapsed", type="password")

    with col2:
        is_submit_pressed = st.button("Submit Key")
        if is_submit_pressed:
            st.session_state["GOOGLE_API_KEY"] = api_key.strip()
            
    os.environ["GOOGLE_API_KEY"] = st.session_state["GOOGLE_API_KEY"]

    if not st.session_state["GOOGLE_API_KEY"]:
        st.stop()
    st.rerun()


@st.cache_resource
def load_llm():
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            system_instruction=BALI_GO_PERSONA
        )
        return llm
    except Exception as e:
        st.error(f"Gagal memuat model. Pastikan API Key Anda valid. Error: {e}")
        return None

def get_chat_history():
    if "chat_history" not in st.session_state:
        welcome_message = AIMessage(
            content="Halo! Saya Bali Go, asisten wisata pribadi Anda di Pulau Dewata. "
                    "Ada yang bisa saya bantu untuk merencanakan liburan Anda ke Bali hari ini?"
        )
        st.session_state["chat_history"] = [welcome_message]
    return st.session_state["chat_history"]


def display_chat_message(message):
    if isinstance(message, HumanMessage):
        role = "user"
    elif isinstance(message, AIMessage):
        role = "assistant"
    else:
        return
        
    with st.chat_message(role):
        st.markdown(message.content)


def display_chat_history(chat_history):
    for chat in chat_history:
        display_chat_message(chat)


def user_query_to_llm(llm, chat_history):
    prompt = st.chat_input("Tanyakan tentang Bali...")
    
    if not prompt:
        return

    human_message = HumanMessage(content=prompt)
    chat_history.append(human_message)
    display_chat_message(human_message)

    with st.spinner("Bali Go sedang berpikir..."):
        try:
            response = llm.invoke(chat_history)
        except Exception as e:
            error_msg = f"Terjadi kesalahan saat berkomunikasi dengan Gemini. Pastikan API Key benar. Error: {e}"
            response = AIMessage(content=error_msg)
            
    chat_history.append(response)
    display_chat_message(response)
    st.rerun()


def main():
    get_api_key_input()
    
    llm = load_llm()
    if not llm:
        st.stop()

    chat_history = get_chat_history()
    
    display_chat_history(chat_history)
    
    user_query_to_llm(llm, chat_history)


if __name__ == "__main__":
    main()
