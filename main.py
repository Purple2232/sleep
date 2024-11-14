import streamlit as st

# App title and introduction
st.title("Promoting Healthy Light and Screen Use Habits")
st.write("""
This tool helps assess your screen use habits, readiness to adopt healthier lighting and screen practices, and provides tailored support to help you make informed choices for your well-being.
""")

# Section 1: Screen Use Habits Assessment
st.header("Step 1: Understanding Your Screen Use Habits")

# Expanded questions in Step 1
# Question 1: Estimated hours of daily screen time
screen_time = st.selectbox("How many hours a day do you estimate you spend with screens?", 
                           options=["Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "More than 8 hours"])

# Question 2: Devices frequently used
devices = st.multiselect("Which of these devices do you interact with daily? Select all that apply.",
                         options=["Smartphone", "Tablet", "Laptop", "Desktop Computer", "Television", "Smart Watch", "E-Reader", "Gaming Console", "Other"])

# Question 3: Awareness of potential health effects
awareness = st.radio("Are you aware of any potential health impacts from frequent screen use?",
                     options=["Yes, I am aware", "No, I am not aware", "I've heard some information"])

# Additional questions in Step 1
handheld_with_lights = st.radio("Do you use handheld devices while other lights are on?",
                                options=["Yes", "No", "Sometimes"])

screen_time_dark = st.radio("Do you often use your devices in the dark?",
                            options=["Yes", "No", "Sometimes"])

phone_morning = st.radio("Do you use your phone first thing in the morning?", 
                         options=["Yes", "No"])

phone_bedtime = st.radio("How long do you use your phone before going to sleep?", 
                         options=["Less than 10 minutes", "10-30 minutes", "30-60 minutes", "More than 1 hour"])

morning_wait_time = st.selectbox("How long do you wait after waking up before using your phone?",
                                 options=["Immediately", "Within 15 minutes", "15-30 minutes", "More than 30 minutes"])

electronics_before_bed = st.radio("How many hours before bed do you stop using electronics?",
                                  options=["I use them until bed", "30 minutes", "1 hour", "2+ hours"])

device_distance = st.radio("At what distance do you typically view your devices?",
                           options=["Less than 12 inches", "12-18 inches", "18-24 inches", "More than 24 inches"])

eye_insurance = st.radio("Do you have eye care insurance or regularly visit an eye care professional?", 
                         options=["Yes", "No"])

# Calculate the Screen Use Score with additional questions
score = 0
if screen_time == "Less than 2 hours":
    score += 10
elif screen_time == "2-4 hours":
    score += 20
elif screen_time == "4-6 hours":
    score += 40
elif screen_time == "6-8 hours":
    score += 60
else:
    score += 80
score += len(devices) * 5
if awareness != "No, I am not aware":
    score += 10
if handheld_with_lights == "Yes":
    score += 5
if screen_time_dark == "Yes":
    score += 10
if phone_morning == "Yes":
    score += 5
if phone_bedtime == "More than 1 hour":
    score += 10
elif phone_bedtime == "30-60 minutes":
    score += 5
if morning_wait_time == "Immediately":
    score += 10
elif morning_wait_time == "Within 15 minutes":
    score += 5
if electronics_before_bed == "I use them until bed":
    score += 10
if device_distance == "Less than 12 inches":
    score += 10
elif device_distance == "12-18 inches":
    score += 5
if eye_insurance == "Yes":
    score -= 5
score = min(score, 100)

# Display score and provide initial feedback
st.write("### Your Screen Use Score: ", score, "%")
if score > 50:
    st.write("Your screen use habits indicate room for improvement. Below, we’ll provide tailored suggestions to support healthier habits.")

# Section 2: Readiness Assessment
st.header("Step 2: Assess Your Awareness and Readiness")

# Awareness scale
awareness_scale = st.radio("How would you rate your awareness of health impacts related to artificial light and screen use?",
                           options=["Very aware", "Slightly aware", "Minimally aware", "No awareness"])

# Additional Readiness Questions
readiness_desire = st.radio("How interested are you in learning more or taking steps to reduce health impacts?",
                            options=["Not interested", "Considering it", "Would like to but unsure how", "Actively taking steps"])

readiness_actions_taken = st.radio("Have you taken any steps to reduce potential health impacts of screen and light use?",
                                   options=["None", "Thinking about it", "Some steps", "Consistent changes"])

barriers = st.multiselect("What barriers prevent you from reducing screen time? Select all that apply.",
                          options=["Work or study requirements", "Entertainment", "Communication needs", "Habits or routines", "Lack of awareness", "Cost of alternatives", "Other"])

# Determine readiness stage based on responses
if awareness_scale == "No awareness" and readiness_desire == "Not interested":
    stage = "New to the Topic"
elif awareness_scale in ["Minimally aware", "Slightly aware"] and readiness_desire in ["Considering it", "Would like to but unsure how"]:
    stage = "Curious but Unsure"
elif awareness_scale == "Very aware" and readiness_desire == "Would like to but unsure how":
    stage = "Aware but Seeking Guidance"
elif awareness_scale == "Very aware" and readiness_desire == "Actively taking steps" and readiness_actions_taken in ["Some steps", "Consistent changes"]:
    stage = "Taking Positive Steps"
else:
    stage = "Balanced and Knowledgeable"

# Step 3: Personalized Support Based on Readiness Stage
st.header("Step 3: Your Personalized Support and Recommendations")
st.write(f"Based on your responses, here are some tailored suggestions to support your journey to healthier screen and light habits.")

# Detailed Recommendations and Support for All Stages
st.subheader("Comprehensive Recommendations")

st.write("""
Here’s a range of strategies and insights to help you manage your screen time and light exposure effectively and sustainably:

- **Exposure to Natural Sunlight**:
  - Morning sunlight is particularly beneficial for setting your body’s internal clock, leading to more consistent melatonin production. This hormone not only regulates sleep but also supports antioxidant function, immune health, and hormone balance.
  - Aim for 10-30 minutes of sunlight exposure each morning, ideally within an hour of waking. This simple habit can improve mood, boost alertness, and regulate sleep-wake cycles.

- **Blue Light Management**:
  - Blue light exposure in the evening can interfere with melatonin production. Consider using blue light blocking glasses if you use screens at night, or activate blue light filters on your devices.
  - Try the **“cool light during day, warm light at night”** principle: use warmer lighting (3000K or lower) in the evening and cool, daylight-mimicking light (5000K or above) during daytime hours.
  - Use apps like [f.lux](https://justgetflux.com) or your device’s built-in settings to adjust screen temperature automatically.

- **Optimize Bedroom Lighting**:
  - Avoid bright overhead lights in the evening; instead, use dimmable lamps with low Kelvin (K) values (under 3000K) to reduce light intensity and keep your body prepared for sleep.
  - When choosing bedroom bulbs, check for adjustable “warm light” options, as cooler lights can interfere with your natural circadian rhythm.

- **Limit Screen Time Before Bed**:
  - Reduce electronic use at least 30 minutes before bed to allow your body to wind down.
  - If you use screens close to bedtime, consider dimming the brightness and using night-mode or dark-mode settings.
  - Create a consistent nighttime routine that does not include screens to help signal to your body that it’s time for rest.

- **Incorporate Eye Care Practices**:
  - Use the **20-20-20 rule**: Every 20 minutes, take a 20-second break and look at something 20 feet away.
  - Practice eye exercises such as gently rolling your eyes, blinking more often, or focusing on near and far objects to reduce eye strain.
  - Regular visits to an eye care professional can help detect any issues related to prolonged screen use early on.

- **Set Boundaries Around Screen Use**:
  - Set boundaries for device usage, especially during meals, breaks, or family time.
  - Allocate certain times or activities as “screen-free zones,” like the first hour in the morning or during evening relaxation times.
  - Try using physical timers or apps that limit app usage to help maintain these boundaries.

- **Check Light Packaging and Color Temperature**:
  - Review the correlated color temperature (CCT) on lighting products and opt for lights under 3000K for evening use.
  - Higher CCT lights (4000K or more) are beneficial for daytime but should be dimmed or avoided at night.

- **Engage in Physical Activity**:
  - Physical activity, particularly during daylight hours, helps reduce the impact of prolonged screen time by promoting circulation, reducing stress, and helping you sleep better.
  - Even short breaks for stretching or walking around can counteract the sedentary effects of screen time.

- **Consider Ergonomic and Adjustable Lighting**:
  - Desk lamps with adjustable brightness and color temperature settings can help minimize eye strain and maintain circadian health.
  - Position screens at eye level and about an arm’s length away to promote better posture and reduce strain.

- **Apps to Track and Manage Light Exposure**:
  - Apps like **Iris** and **Twilight** can help adjust screen color temperature based on the time of day, supporting a healthier light environment.
  - Sleep-tracking apps can monitor sleep quality, giving feedback on how your light habits may be affecting rest.

- **Educate Yourself on the Health Impacts of Light**:
  - Learn more about the impacts of artificial light on health through reputable sources like [DarkSky.org](https://www.darksky.org), which discusses light pollution and its effects.
  - Keep up-to-date with research or articles on eye health and circadian science to understand new strategies and recommendations.

""")

# Additional future directions for the app
st.subheader("Future Directions for This Application")

st.write("""
To further support users and make the journey to healthier light and screen habits engaging and rewarding, here are some potential enhancements:

- **Habit Tracking and Progress Monitoring**:
  - Enable users to track their screen time, breaks, and light management habits over time, providing insights into improvement areas and celebrating progress.

- **Personalized Reminders and Notifications**:
  - Set reminders for taking screen breaks, enabling blue light filters, or starting wind-down routines before bed to help build consistent habits.

- **Reward System**:
  - Introduce rewards or incentives, such as digital badges or points, that users can earn for reaching screen use reduction milestones or completing specific challenges.
  - Consider integrating with services that offer discounts on eye care products, ergonomic lighting, or blue light glasses.

- **Community Support and Sharing**:
  - Allow users to connect with others who are on similar health journeys, sharing tips and successes or discussing strategies for managing screen use.
  - Introduce a community leaderboard for encouragement, where users can see their progress compared to others.

- **Customized Goal-Setting**:
  - Allow users to set specific screen use or light exposure goals based on their preferences and provide step-by-step guidance to achieve those goals.

- **In-Depth Educational Content**:
  - Expand the app to include more articles, videos, and guides on the science behind light and sleep health, covering topics like photoreceptors, circadian rhythms, and practical tips for sustainable screen use.

- **Advanced Insights and Reports**:
  - Provide detailed monthly reports that track usage patterns, compare them to optimal ranges, and suggest personalized adjustments to improve health outcomes.

- **AI-Driven Recommendations**:
  - Use AI to analyze user habits and generate tailored recommendations that evolve as the user’s habits change, providing dynamic support that adapts to their progress.

- **Integration with Wearable Devices**:
  - Integrate with wearable devices or health apps to automatically track screen exposure, light intensity, and sleep quality for a more comprehensive health picture.

This app aims to empower users by creating a balanced approach to screen and light use that supports their health while respecting modern lifestyle demands.
""")

st.write("Thank you for using this app! We hope it provides a supportive way to enhance your screen habits without stress and looks forward to providing even more personalized support in the future.")
