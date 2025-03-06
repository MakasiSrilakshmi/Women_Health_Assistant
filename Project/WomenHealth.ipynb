import tkinter as tk
from tkinter import messagebox, Scrollbar
from joblib import load
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai
from PIL import Image, ImageTk  # Import Pillow for JPG support
from datetime import datetime  # Import datetime for timestamping treatments

# Configure Gemini API
genai.configure(api_key="API KEY")  # Replace with your Gemini API key

# Initialize Gemini model
gemini_model = genai.GenerativeModel('gemini-2.0-flash')

# Function to interact with Gemini
def ask_gemini(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Load pre-trained models and scalers for each disease
def load_models():
    models = {
        "Diabetes": {
            "scaler": load('diabetes_scaler.joblib'),  # Relative path
            "model": load('diabetes_kmeans.joblib')   # Relative path
        },
        "Heart Disease": {
            "scaler": load('heart_disease_scaler.joblib'),  # Relative path
            "model": load('heart_disease_kmeans.joblib')    # Relative path
        },
        "Cervical Cancer": {
            "scaler": load('cervical_cancer_scaler.joblib'),  # Relative path
            "model": load('cervical_cancer_kmeans.joblib')     # Relative path
        }
    }
    return models

# Function to predict cluster and generate recommendations
def predict_cluster():
    disease = disease_var.get()
    symptoms = []

    try:
        if disease == "Diabetes":
            symptoms = [
                float(entry_pregnancies.get()),
                float(entry_glucose.get()),
                float(entry_blood_pressure.get()),
                float(entry_skin_thickness.get()),
                float(entry_insulin.get()),
                float(entry_bmi.get()),
                float(entry_diabetes_pedigree.get()),
                float(entry_age.get())
            ]
        elif disease == "Heart Disease":
            symptoms = [
                float(entry_age.get()),
                float(entry_sex.get()),
                float(entry_cp.get()),
                float(entry_trestbps.get()),
                float(entry_chol.get()),
                float(entry_fbs.get()),
                float(entry_restecg.get()),
                float(entry_thalach.get()),
                float(entry_exang.get()),
                float(entry_oldpeak.get()),
                float(entry_slope.get()),
                float(entry_ca.get()),
                float(entry_thal.get())
            ]
        elif disease == "Cervical Cancer":
            symptoms = [
                float(entry_age.get()),
                float(entry_sexual_partners.get()),
                float(entry_first_sexual_intercourse.get()),
                float(entry_num_pregnancies.get()),
                float(entry_smokes.get()),
                float(entry_smokes_years.get()),
                float(entry_smokes_packs_year.get()),
                float(entry_hormonal_contraceptives.get()),
                float(entry_hormonal_contraceptives_years.get()),
                float(entry_iud.get()),
                float(entry_iud_years.get()),
                float(entry_std.get()),
                float(entry_std_number.get())
            ]

        # Get the model and scaler for the selected disease
        scaler = models[disease]["scaler"]
        model = models[disease]["model"]

        # Preprocess input
        symptoms_scaled = scaler.transform([symptoms])

        # Predict cluster
        cluster = model.predict(symptoms_scaled)[0]

        # Get previous medical history
        previous_history = entry_previous_history.get("1.0", tk.END).strip()

        # Generate recommendations using Gemini
        prompt = f"""
        A user concerned about their health has received an assessment for {disease} and is placed in cluster {cluster}.
        Previous Medical History: {previous_history}
        Provide **2-3 very short, direct, and reassuring recommendations** focusing on **immediate, actionable steps** they can take to manage their health and wellbeing.
        Prioritize practical self-care and encourage seeking professional medical advice for further evaluation.
        Keep the language user-friendly and avoid overly technical terms.
        """
        recommendations = ask_gemini(prompt)

        # Determine risk level and color
        risk_level = "High Risk" if cluster == 1 else "Low Risk"
        risk_color = "red" if cluster == 1 else "blue"

        # Show the result with color-coded risk level
        result = f"Cluster: {cluster} ({risk_level})\nRecommendation: {recommendations}"
        messagebox.showinfo("Cluster Prediction", result)

        # Save prediction to history
        prediction_history.append((disease, result, risk_color))
        update_dashboard()

        # Send notification
        send_notification(result)

    except ValueError:
        messagebox.showerror("Input Error", "Please fill in all fields with numeric values.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to send email notification
def send_notification(message, is_reminder=False):
    email = entry_email.get()
    phone = entry_phone.get()

    if email:
        try:
            # Email configuration
            smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
            smtp_port = 587  # Replace with your SMTP port
            sender_email = "your_email@gmail.com"  # Replace with your email
            sender_password = "your_password"  # Replace with your email password

            # Create the email
            subject = "Reminder Notification" if is_reminder else "Disease Prediction Notification"
            body = f"Dear {entry_name.get()},\n\n{message}\n\nBest regards,\nYour Health Team"

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
            print(f"Email sent to {email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    if phone:
        print(f"Simulating SMS to {phone}: {message}")

# Function to set a reminder
def set_reminder():
    # Create a new window for setting reminders
    reminder_window = tk.Toplevel(root)
    reminder_window.title("Set Reminder")
    reminder_window.configure(bg="#E0F7FA")

    # Add input fields for reminder details
    tk.Label(reminder_window, text="Reminder Time (HH:MM):", bg="#E0F7FA").grid(row=0, column=0, padx=10, pady=10)
    entry_reminder_time = tk.Entry(reminder_window)
    entry_reminder_time.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(reminder_window, text="Reminder Message:", bg="#E0F7FA").grid(row=1, column=0, padx=10, pady=10)
    entry_reminder_message = tk.Entry(reminder_window)
    entry_reminder_message.grid(row=1, column=1, padx=10, pady=10)

    # Function to handle the reminder submission
    def submit_reminder():
        reminder_time = entry_reminder_time.get()
        reminder_message = entry_reminder_message.get()

        if reminder_time and reminder_message:
            # Simulate sending a reminder notification
            send_notification(f"Reminder: {reminder_message}", is_reminder=True)
            messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time}.")
            reminder_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    # Add a submit button
    tk.Button(reminder_window, text="Set Reminder", command=submit_reminder, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Function to update input fields based on disease selection
def update_input_fields():
    disease = disease_var.get()
    # Hide all input fields
    for widget in input_frame.winfo_children():
        widget.grid_remove()

    # Show relevant input fields
    if disease == "Diabetes":
        tk.Label(input_frame, text="Pregnancies:", bg="#E0F7FA").grid(row=0, column=0)
        entry_pregnancies.grid(row=0, column=1)
        tk.Label(input_frame, text="Glucose:", bg="#E0F7FA").grid(row=1, column=0)
        entry_glucose.grid(row=1, column=1)
        tk.Label(input_frame, text="Blood Pressure:", bg="#E0F7FA").grid(row=2, column=0)
        entry_blood_pressure.grid(row=2, column=1)
        tk.Label(input_frame, text="Skin Thickness:", bg="#E0F7FA").grid(row=3, column=0)
        entry_skin_thickness.grid(row=3, column=1)
        tk.Label(input_frame, text="Insulin:", bg="#E0F7FA").grid(row=4, column=0)
        entry_insulin.grid(row=4, column=1)
        tk.Label(input_frame, text="BMI:", bg="#E0F7FA").grid(row=5, column=0)
        entry_bmi.grid(row=5, column=1)
        tk.Label(input_frame, text="Diabetes Pedigree Function:", bg="#E0F7FA").grid(row=6, column=0)
        entry_diabetes_pedigree.grid(row=6, column=1)
        tk.Label(input_frame, text="Age:", bg="#E0F7FA").grid(row=7, column=0)
        entry_age.grid(row=7, column=1)

    elif disease == "Heart Disease":
        tk.Label(input_frame, text="Age:", bg="#E0F7FA").grid(row=0, column=0)
        entry_age.grid(row=0, column=1)
        tk.Label(input_frame, text="Sex (0=Female, 1=Male):", bg="#E0F7FA").grid(row=1, column=0)
        entry_sex.grid(row=1, column=1)
        tk.Label(input_frame, text="Chest Pain Type (0-3):", bg="#E0F7FA").grid(row=2, column=0)
        entry_cp.grid(row=2, column=1)
        tk.Label(input_frame, text="Resting Blood Pressure:", bg="#E0F7FA").grid(row=3, column=0)
        entry_trestbps.grid(row=3, column=1)
        tk.Label(input_frame, text="Cholesterol:", bg="#E0F7FA").grid(row=4, column=0)
        entry_chol.grid(row=4, column=1)
        tk.Label(input_frame, text="Fasting Blood Sugar (>120 mg/dl=1):", bg="#E0F7FA").grid(row=5, column=0)
        entry_fbs.grid(row=5, column=1)
        tk.Label(input_frame, text="Resting ECG Results (0-2):", bg="#E0F7FA").grid(row=6, column=0)
        entry_restecg.grid(row=6, column=1)
        tk.Label(input_frame, text="Max Heart Rate Achieved:", bg="#E0F7FA").grid(row=7, column=0)
        entry_thalach.grid(row=7, column=1)
        tk.Label(input_frame, text="Exercise Induced Angina (1=Yes, 0=No):", bg="#E0F7FA").grid(row=8, column=0)
        entry_exang.grid(row=8, column=1)
        tk.Label(input_frame, text="ST Depression Induced by Exercise:", bg="#E0F7FA").grid(row=9, column=0)
        entry_oldpeak.grid(row=9, column=1)
        tk.Label(input_frame, text="Slope of Peak Exercise ST Segment (0-2):", bg="#E0F7FA").grid(row=10, column=0)
        entry_slope.grid(row=10, column=1)
        tk.Label(input_frame, text="Number of Major Vessels Colored by Fluoroscopy (0-3):", bg="#E0F7FA").grid(row=11, column=0)
        entry_ca.grid(row=11, column=1)
        tk.Label(input_frame, text="Thalassemia (1-3):", bg="#E0F7FA").grid(row=12, column=0)
        entry_thal.grid(row=12, column=1)

    elif disease == "Cervical Cancer":
        tk.Label(input_frame, text="Age:", bg="#E0F7FA").grid(row=0, column=0)
        entry_age.grid(row=0, column=1)
        tk.Label(input_frame, text="Number of Sexual Partners:", bg="#E0F7FA").grid(row=1, column=0)
        entry_sexual_partners.grid(row=1, column=1)
        tk.Label(input_frame, text="First Sexual Intercourse (age):", bg="#E0F7FA").grid(row=2, column=0)
        entry_first_sexual_intercourse.grid(row=2, column=1)
        tk.Label(input_frame, text="Number of Pregnancies:", bg="#E0F7FA").grid(row=3, column=0)
        entry_num_pregnancies.grid(row=3, column=1)
        tk.Label(input_frame, text="Smokes (0=No, 1=Yes):", bg="#E0F7FA").grid(row=4, column=0)
        entry_smokes.grid(row=4, column=1)
        tk.Label(input_frame, text="Smokes (years):", bg="#E0F7FA").grid(row=5, column=0)
        entry_smokes_years.grid(row=5, column=1)
        tk.Label(input_frame, text="Smokes (packs/year):", bg="#E0F7FA").grid(row=6, column=0)
        entry_smokes_packs_year.grid(row=6, column=1)
        tk.Label(input_frame, text="Hormonal Contraceptives (0=No, 1=Yes):", bg="#E0F7FA").grid(row=7, column=0)
        entry_hormonal_contraceptives.grid(row=7, column=1)
        tk.Label(input_frame, text="Hormonal Contraceptives (years):", bg="#E0F7FA").grid(row=8, column=0)
        entry_hormonal_contraceptives_years.grid(row=8, column=1)
        tk.Label(input_frame, text="IUD (0=No, 1=Yes):", bg="#E0F7FA").grid(row=9, column=0)
        entry_iud.grid(row=9, column=1)
        tk.Label(input_frame, text="IUD (years):", bg="#E0F7FA").grid(row=10, column=0)
        entry_iud_years.grid(row=10, column=1)
        tk.Label(input_frame, text="STDs (0=No, 1=Yes):", bg="#E0F7FA").grid(row=11, column=0)
        entry_std.grid(row=11, column=1)
        tk.Label(input_frame, text="Number of STDs:", bg="#E0F7FA").grid(row=12, column=0)
        entry_std_number.grid(row=12, column=1)

    # Add previous medical history input field
    tk.Label(input_frame, text="Previous Medical History:", bg="#E0F7FA").grid(row=13, column=0)
    global entry_previous_history
    entry_previous_history = tk.Text(input_frame, height=5, width=40)
    entry_previous_history.grid(row=13, column=1)

    # Add Treatment/Test Recording section
    tk.Label(input_frame, text="Record Treatment/Test:", font=("Arial", 12, "bold"), bg="#E0F7FA").grid(row=14, column=0, columnspan=2, pady=(10,0))
    tk.Label(input_frame, text="Treatment/Test Name:", bg="#E0F7FA").grid(row=15, column=0)
    global entry_treatment_name
    entry_treatment_name = tk.Entry(input_frame)
    entry_treatment_name.grid(row=15, column=1)
    tk.Label(input_frame, text="Date (YYYY-MM-DD):", bg="#E0F7FA").grid(row=16, column=0)
    global entry_treatment_date
    entry_treatment_date = tk.Entry(input_frame)
    entry_treatment_date.grid(row=16, column=1)
    tk.Label(input_frame, text="Results/Notes:", bg="#E0F7FA").grid(row=17, column=0)
    global entry_treatment_notes
    entry_treatment_notes = tk.Text(input_frame, height=3, width=40)
    entry_treatment_notes.grid(row=17, column=1)
    global record_treatment_button
    record_treatment_button = tk.Button(input_frame, text="Record Treatment", command=record_treatment, bg="#00BCD4", fg="white", font=("Arial", 10, "bold")) # Teal color
    record_treatment_button.grid(row=18, column=0, columnspan=2, pady=(5,10))

# Function to record treatment/test information
def record_treatment():
    disease = disease_var.get()
    treatment_name = entry_treatment_name.get()
    treatment_date_str = entry_treatment_date.get()
    treatment_notes = entry_treatment_notes.get("1.0", tk.END).strip()

    try:
        treatment_date = datetime.strptime(treatment_date_str, '%Y-%m-%d').date() # Validate date format
        treatment_details = {
            "name": treatment_name,
            "date": treatment_date.strftime('%Y-%m-%d'), # Store date as string for simplicity
            "notes": treatment_notes
        }
        treatment_history.append((disease, treatment_details))
        update_dashboard()
        messagebox.showinfo("Treatment Recorded", "Treatment/Test information recorded successfully.")
        # Clear treatment input fields after recording
        entry_treatment_name.delete(0, tk.END)
        entry_treatment_date.delete(0, tk.END)
        entry_treatment_notes.delete("1.0", tk.END)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter date in YYYY-MM-DD format.")
    except Exception as e:
        messagebox.showerror("Error", f"Error recording treatment: {e}")


# Function to update the dashboard
def update_dashboard():
    for widget in dashboard_scrollable_frame.winfo_children(): # Use scrollable frame here
        widget.destroy()

    tk.Label(dashboard_scrollable_frame, text="User Information", font=("Arial", 14, "bold"), bg="#E0F7FA").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(dashboard_scrollable_frame, text=f"Name: {entry_name.get()}", bg="#E0F7FA").grid(row=1, column=0, sticky="w")
    tk.Label(dashboard_scrollable_frame, text=f"Email: {entry_email.get()}", bg="#E0F7FA").grid(row=2, column=0, sticky="w")
    tk.Label(dashboard_scrollable_frame, text=f"Phone: {entry_phone.get()}", bg="#E0F7FA").grid(row=3, column=0, sticky="w")

    tk.Label(dashboard_scrollable_frame, text="Prediction History", font=("Arial", 14, "bold"), bg="#E0F7FA").grid(row=4, column=0, columnspan=2, pady=10)
    for i, (disease, result, risk_color) in enumerate(prediction_history):
        tk.Label(dashboard_scrollable_frame, text=f"{disease}: {result}", bg="#E0F7FA", fg=risk_color).grid(row=5 + i, column=0, sticky="w")

    tk.Label(dashboard_scrollable_frame, text="Treatment History", font=("Arial", 14, "bold"), bg="#E0F7FA").grid(row=len(prediction_history) + 6, column=0, columnspan=2, pady=10) # Position after prediction history
    if treatment_history:
        for i, (disease, treatment_details) in enumerate(treatment_history):
            treatment_text = f"{disease}: {treatment_details['name']} - Date: {treatment_details['date']}"
            if treatment_details['notes']:
                treatment_text += f" - Notes: {treatment_details['notes']}"
            tk.Label(dashboard_scrollable_frame, text=treatment_text, bg="#E0F7FA", anchor="w", justify="left").grid(row=len(prediction_history) + 7 + i, column=0, sticky="ew")
    else:
        tk.Label(dashboard_scrollable_frame, text="No treatment history recorded yet.", bg="#E0F7FA").grid(row=len(prediction_history) + 7, column=0, sticky="w")

    dashboard_scrollable_frame.update_idletasks() # Update to get correct frame size
    dashboard_canvas.config(scrollregion=dashboard_canvas.bbox("all")) # Adjust scroll region


# Function to switch between pages
def show_page(page):
    home_canvas.grid_remove() # Hide canvas instead of frame
    dashboard_canvas.grid_remove() # Hide canvas instead of frame
    page.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew") # Show canvas and use sticky to fill


def home_frame_scroll(event):
    home_canvas.configure(scrollregion=home_canvas.bbox("all"))

def dashboard_frame_scroll(event):
    dashboard_canvas.configure(scrollregion=dashboard_canvas.bbox("all"))


# Load models
models = load_models()

# Create the main window
root = tk.Tk()
root.title("Women Health Assistant")
root.configure(bg="#E0F7FA") # Light Blue Background for root

root.grid_rowconfigure(2, weight=1) # Allow row 2 (canvas row) to expand
root.grid_columnconfigure(0, weight=1) # Allow column 0 to expand


# Add a title and logo
title_frame = tk.Frame(root, bg="#E0F7FA") # Light Blue Background
title_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Load logo using Pillow for JPG support and resize it
try:
    # Use a relative path if the image is in the same directory as the script
    image_path = "download (1).jpg"  # Replace with the correct file name
    image = Image.open(image_path)
    # Resize the image to a smaller size (e.g., 100x100 pixels)
    image = image.resize((100, 100), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(title_frame, image=logo, bg="#E0F7FA") # Light Blue Background
    logo_label.grid(row=0, column=0, padx=10)
    logo_label.image = logo  # Keep a reference to the image
except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'. Please check the file path.")
except Exception as e:
    print(f"Error loading image: {e}")

# Title
tk.Label(title_frame, text="Women Health Assistant", font=("Arial", 24, "bold"), bg="#E0F7FA", fg="#F06292").grid(row=0, column=1, padx=10) # Pink color for title

# Navigation bar
nav_frame = tk.Frame(root, bg="#E0F7FA") # Light Blue Background
nav_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

tk.Button(nav_frame, text="Home", command=lambda: show_page(home_canvas), bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)
tk.Button(nav_frame, text="Dashboard", command=lambda: show_page(dashboard_canvas), bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10)

tk.Button(nav_frame, text="Set Reminder", command=lambda: set_reminder(), bg="#FF9800", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, sticky="e")


# --- Home Frame with Scrollbar ---
home_canvas = tk.Canvas(root, bg="#E0F7FA", bd=0, highlightthickness=0)
home_canvas.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew") # Use grid and sticky to fill

home_scrollbar_y = Scrollbar(root, orient="vertical", command=home_canvas.yview)
home_scrollbar_y.grid(row=2, column=4, sticky="ns")
home_canvas.configure(yscrollcommand=home_scrollbar_y.set)

home_scrollbar_x = Scrollbar(root, orient="horizontal", command=home_canvas.xview)
home_scrollbar_x.grid(row=3, column=0, columnspan=4, sticky="ew")
home_canvas.configure(xscrollcommand=home_scrollbar_x.set)


home_scrollable_frame = tk.Frame(home_canvas, bg="#E0F7FA") # Frame inside canvas
home_canvas.create_window((0, 0), window=home_scrollable_frame, anchor="nw")
home_scrollable_frame.bind("<Configure>", home_frame_scroll)


# Personal information frame (inside scrollable home frame)
personal_info_frame = tk.LabelFrame(home_scrollable_frame, text="Personal Information", bg="#E0F7FA", padx=10, pady=10) # Light Blue Background
personal_info_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

tk.Label(personal_info_frame, text="Name:", bg="#E0F7FA").grid(row=0, column=0)
entry_name = tk.Entry(personal_info_frame)
entry_name.grid(row=0, column=1)

tk.Label(personal_info_frame, text="Email:", bg="#E0F7FA").grid(row=1, column=0)
entry_email = tk.Entry(personal_info_frame)
entry_email.grid(row=1, column=1)

tk.Label(personal_info_frame, text="Phone:", bg="#E0F7FA").grid(row=2, column=0)
entry_phone = tk.Entry(personal_info_frame)
entry_phone.grid(row=2, column=1)

# Disease selection frame (inside scrollable home frame)
disease_frame = tk.LabelFrame(home_scrollable_frame, text="Select Disease", bg="#E0F7FA", padx=10, pady=10) # Light Blue Background
disease_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

disease_var = tk.StringVar(value="Diabetes")
tk.Radiobutton(disease_frame, text="Diabetes", variable=disease_var, value="Diabetes", command=update_input_fields, bg="#E0F7FA").grid(row=0, column=0)
tk.Radiobutton(disease_frame, text="Heart Disease", variable=disease_var, value="Heart Disease", command=update_input_fields, bg="#E0F7FA").grid(row=0, column=1)
tk.Radiobutton(disease_frame, text="Cervical Cancer", variable=disease_var, value="Cervical Cancer", command=update_input_fields, bg="#E0F7FA").grid(row=0, column=2)

# Input fields frame (inside scrollable home frame)
input_frame = tk.Frame(home_scrollable_frame, bg="#E0F7FA") # Light Blue Background
input_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Initialize input fields
entry_pregnancies = tk.Entry(input_frame)
entry_glucose = tk.Entry(input_frame)
entry_blood_pressure = tk.Entry(input_frame)
entry_skin_thickness = tk.Entry(input_frame)
entry_insulin = tk.Entry(input_frame)
entry_bmi = tk.Entry(input_frame)
entry_diabetes_pedigree = tk.Entry(input_frame)
entry_age = tk.Entry(input_frame)
entry_sex = tk.Entry(input_frame)
entry_cp = tk.Entry(input_frame)
entry_trestbps = tk.Entry(input_frame)
entry_chol = tk.Entry(input_frame)
entry_fbs = tk.Entry(input_frame)
entry_restecg = tk.Entry(input_frame)
entry_thalach = tk.Entry(input_frame)
entry_exang = tk.Entry(input_frame)
entry_oldpeak = tk.Entry(input_frame)
entry_slope = tk.Entry(input_frame)
entry_ca = tk.Entry(input_frame)
entry_thal = tk.Entry(input_frame)
entry_sexual_partners = tk.Entry(input_frame)
entry_first_sexual_intercourse = tk.Entry(input_frame)
entry_num_pregnancies = tk.Entry(input_frame)
entry_smokes = tk.Entry(input_frame)
entry_smokes_years = tk.Entry(input_frame)
entry_smokes_packs_year = tk.Entry(input_frame)
entry_hormonal_contraceptives = tk.Entry(input_frame)
entry_hormonal_contraceptives_years = tk.Entry(input_frame)
entry_iud = tk.Entry(input_frame)
entry_iud_years = tk.Entry(input_frame)
entry_std = tk.Entry(input_frame)
entry_std_number = tk.Entry(input_frame)

# Predict button (inside scrollable home frame)
predict_button = tk.Button(home_scrollable_frame, text="Predict", command=predict_cluster, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
predict_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)


# --- Dashboard Frame with Scrollbar ---
dashboard_canvas = tk.Canvas(root, bg="#E0F7FA", bd=0, highlightthickness=0)
dashboard_canvas.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew") # Use grid and sticky to fill

dashboard_scrollbar_y = Scrollbar(root, orient="vertical", command=dashboard_canvas.yview)
dashboard_scrollbar_y.grid(row=2, column=4, sticky="ns")
dashboard_canvas.configure(yscrollcommand=dashboard_scrollbar_y.set)

dashboard_scrollbar_x = Scrollbar(root, orient="horizontal", command=dashboard_canvas.xview)
dashboard_scrollbar_x.grid(row=3, column=0, columnspan=4, sticky="ew")
dashboard_canvas.configure(xscrollcommand=dashboard_scrollbar_x.set)


dashboard_scrollable_frame = tk.Frame(dashboard_canvas, bg="#E0F7FA") # Frame inside canvas
dashboard_canvas.create_window((0, 0), window=dashboard_scrollable_frame, anchor="nw")
dashboard_scrollable_frame.bind("<Configure>", dashboard_frame_scroll)


# Initialize prediction history
prediction_history = []
# Initialize treatment history
treatment_history = []

# Update input fields for initial disease selection
update_input_fields()

# Show home frame by default (show canvas now)
show_page(home_canvas)

# Start the main loop
root.mainloop()