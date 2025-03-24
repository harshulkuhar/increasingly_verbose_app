import logging
from src import gpt_utils, ui_components
import streamlit as st

# Configure the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize UI
ui_components.setup_page()

# Initialize OpenAI client
llm_client = gpt_utils.init_openai()

# Create input section
user_input = ui_components.create_input_section()

if st.button("Get Response"):
    ui_components.handle_response(llm_client, user_input)