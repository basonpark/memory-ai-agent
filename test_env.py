import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Print out the values
print("DATABASE_URL:", os.environ.get('DATABASE_URL', 'Not set'))
print("SUPABASE_URL:", os.environ.get('SUPABASE_URL', 'Not set'))
print("SUPABASE_KEY:", os.environ.get('SUPABASE_KEY', 'Not set'))
print("OPENAI_API_KEY:", os.environ.get('OPENAI_API_KEY', 'Not set')[:10] + '...' if os.environ.get('OPENAI_API_KEY') else 'Not set')
print("MODEL_CHOICE:", os.environ.get('MODEL_CHOICE', 'Not set')) 