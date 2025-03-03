import streamlit as st
from datetime import datetime

# page title
st.set_page_config(page_title=" Ramadan Mubarak 🌙", layout="wide")

# Ramazan greeting
st.header("🌙 Ramadan Mubarak 🕌")
st.write("""**Ramadan** is a journey of patience and gratitude, where each prayer lifts the spirit and every sunset. 
         brings hope and peace. It's a month of self-purification, where kindness blooms and generosity fills the air.""")

#  navigation bar

st.sidebar.title("Navigaion")
# Sidebar with emojis
page = st.sidebar.radio("Go to", [
    "🏠 Home", 
    "🕌 Ramadan Timetable", 
    "🌙 Fasting Tips", 
    "📿 Dua of the Day", 
    "🖼️ Gallery", 
    "📞 Contact Us"
])


#  home section
if page == "🏠 Home":
    st.header("What is Ramadan?")
    st.write("""
Ramadan is the ninth month of the Islamic lunar calendar and is considered one of the holiest months for Muslims. It is a time of fasting, prayer, reflection, and community. Here are some key aspects of Ramadan.
    """)
    
    st.header("Key Aspects of Ramadan:")
    st.write("**1. Fasting:** Ramadan is the holiest month in Islam, marked by fasting from dawn to sunset.")
    st.write("**2. Prayer and Worship**: Muslims focus on prayer, reading the Qur'an, and engaging in extra worship.")
    st.write("**3.Charity:** Charity is emphasized, with Zakat (obligatory) and Sadaqah (voluntary) given to those in need.")
    st.write("**4. Eid al-Fitr:** The end of Ramadan is celebrated with Eid al-Fitr, a festival of feasting and prayers.")
    st.write("**5. Spiritual Growth:** Ramadan promotes spiritual growth, self-discipline, and empathy.")
    
    # Ramadan Timetable section

elif page == "🕌 Ramadan Timetable":
    st.header("🕰️ Ramadan Timetable")
    
    #  Display today's date
    today_date = datetime.now().strftime("%B %d, %Y")
    st.subheader(f"Today's Date: {today_date}")
    
    # Interactive Iftar Countdown
    iftar_time = datetime.strptime('18:45', '%H:%M').time()  
    time = datetime.now()
    # Set actual Iftar time here
    iftar_datetime = datetime.combine(time.date(), iftar_time)
    left_time = iftar_datetime - time
    
    
    hours_left = left_time.seconds // 3600
    minutes_left = (left_time.seconds % 3600) // 60
    st.subheader(f"⏳ Time Left Until Iftar: {hours_left} hours and {minutes_left} minutes")
   
    #  Prayer Timetable
    
    # Placeholder timetable (example)
    st.write("**Today's Prayer Times**")
    prayer_timetable = {
        "Fajr": "04:45 AM",
        "Dhuhr": "12:30 PM",
        "Asr": "04:00 PM",
        "Maghrib (Iftar)": "06:50 PM",
        "Isha": "08:15 PM"
    }
    
    for prayer, time in prayer_timetable.items():
        st.write(f"**{prayer}:** {time}")
        
    
    
    
     
    
    #  fasting tip section
elif page =="🌙 Fasting Tips":
    st.header("📖 Tips For Fasting During Ramadan")
    st.write("""
    Here are some helpful tips for fasting during the month of Ramadan:
    
    1. **Hydrate**: Drink plenty of water during Suhoor and Iftar to stay hydrated throughout the day.
    2. **Balanced Diet**: Eat balanced meals with proteins, carbohydrates, and healthy fats to maintain energy.
    3. **Avoid Overeating**: Try not to overeat during Iftar to avoid fatigue.
    4. **Rest**: Get enough rest at night to have the energy to fast the next day.
    5. **Prayers and Patience**: Remember the spiritual significance of fasting and pray regularly.
    """)
    
    #  Dua of the day section
elif page ==  "📿 Dua of the Day":
    st.header("📿 Dua of the Day")
    
    # Display a sample Dua
    dua = """
    اللَّهُمَّ إِنِّي لَكَ صُمْتُ وَبِكَ آمَنْتُ وَعَلَيْكَ تَوَكَّلْتُ وَعَلَىٰ رِزْقِكَ أَفْطَرْتُ
    """
    st.write(f"**Dua for Breaking the Fast (Iftar)**: {dua}")
    
    st.write("""
    **Translation**: "O Allah! I fasted for You, and I believe in You, and I put my trust in You, and with Your sustenance, I break my fast."
    """)
    
elif page =="🖼️ Gallery":
    st.header("📷 Ramadan Gallery")
    st.write("Here are some beautiful images that capture the essence of Ramadan.") 
    
      # Add images related to Ramadan
    st.image("https://img.freepik.com/free-psd/ramadan-mubarak-3d-banner-design-template_47987-19386.jpg", caption="Ramadan Karee", use_container_width=True)
    st.image("https://png.pngtree.com/thumb_back/fh260/background/20250120/pngtree-iftar-festivity-for-ramadan-kareem-context-image_16937849.jpg", caption="Iftar Time", use_container_width=True)
    st.image("https://www.dhakarachi.org/wp-content/uploads/2022/06/SJM_0629-1.jpg", caption="Beautiful Mosque", use_container_width=True)


elif page =="📞 Contact Us":
    st.subheader("Contact Us 📞")
    st.write("Feel free to contact us using the form below:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Submit"):
        st.write(f"Thank you {name}, we have received your message!")
      
      
        
#  footer section
st.markdown("""
 ---
🌙 **Ramadan Mubarak** to all! May this month bring you peace, prosperity, and blessings. 🙏
""")    
    
    
    
    
