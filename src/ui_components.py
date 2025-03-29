import streamlit as st
import logging
import openai
from . import gpt_utils

logger = logging.getLogger(__name__)

def setup_page():
    st.set_page_config(page_title="Increasingly Verbose App", layout="wide")
    
    # About section in sidebar
    with st.sidebar:
        st.header("About")
        st.markdown("""
        ### Overview
        This application converts simple sentences into more elaborate versions
        
        ### Usage
        1. Enter your text in the input area
        2. Click 'Get Response'
        3. View the transformed text
        
        ### Sample Inputs
        - Simple statements
        - Questions
        - Short phrases
        """)
    
    st.title("Increasingly Verbose App")

def create_input_section():
    user_input = st.text_area("Write something to make it verbose :")
    return user_input

def handle_response(llm_client, user_input):
    if user_input.strip():  # Ensure it's not empty
        with st.spinner("Thinking..."):
            try:
                # First cache check with original text
                cached = gpt_utils._cache_manager.get_cached_response(user_input)
                if cached:
                    logger.info("Cache hit! Returning cached response ..")
                    verbose_sentence = cached[1]
                else:
                    # If no cache hit, get filtered sentence
                    filtered_sentence = gpt_utils.exclude_instruction(client=llm_client, text_prompt=user_input)
                    
                    # Second cache check with filtered sentence
                    cached = gpt_utils._cache_manager.get_cached_response(filtered_sentence)
                    if cached:
                        logger.info("Cache hit after parsing! Returning cached response ..")
                        verbose_sentence = cached[1]
                    else:
                        # If still no cache hit, proceed with make_verbose
                        verbose_sentence = gpt_utils.make_verbose(client=llm_client, parsed_sentence=filtered_sentence, original_text=user_input)
            except openai.OpenAIError as e:
                logger.critical(f"Code failed somewhere :: {e}")
                verbose_sentence = "Seems like an issue on OpenAI's side. Please try again after a while."
            st.subheader("Response:")
            st.write(verbose_sentence)
    else:
        st.warning("Please enter a sentence before clicking the button.")
