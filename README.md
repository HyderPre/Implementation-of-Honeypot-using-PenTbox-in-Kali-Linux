# Installation of Honeypot using PenTBox in Kali Linux

## 📌 Information Security IA_1

### Group Members:
- **Hyder Presswala** - 16010122151  


---

## 📌 Introduction

### Kali Linux
Kali Linux is a **Debian-based** Linux distribution designed for **penetration testing** and **digital forensics**. It is maintained by **Offensive Security** and includes **over 600 penetration-testing tools**, such as:  
- **Armitage** – Cyber attack management tool  
- **Nmap** – Network scanner  
- **Wireshark** – Packet analyzer  
- **John the Ripper** – Password cracker  
- **SQLMap** – SQL injection testing  
- **Aircrack-ng** – Wireless network security tool  
- **Burp Suite & OWASP ZAP** – Web security tools  

Kali Linux was developed by **Mati Aharoni** and **Devon Kearns** as a rewrite of **BackTrack**, a previous Linux distribution used for security testing.

---

### 🛡️ Honeypot
A **honeypot** is a **decoy system** used to attract hackers and **study their attack patterns**. Organizations use honeypots for **cybersecurity research and threat intelligence**.  

Honeypots help:
✅ Identify **attackers' methods**  
✅ Monitor **unauthorized access attempts**  
✅ Reduce the risk of **real system breaches**  
✅ Improve **network security defenses**  

---

### ⚡ What is PenTBox?
**PenTBox** is an open-source **penetration testing toolkit** written in **Ruby**. It includes tools for:  
- **Honeypots** 🛡️ (Detect unauthorized access attempts)  
- **Hash Cracking** 🔓 (Break MD5, SHA1, etc.)  
- **DNS Enumeration** 🌎 (Gather domain information)  
- **Stress Testing** 💥 (Simulate DoS attacks)  
- **HTTP Directory Brute-Forcing** 🔎 (Find hidden web directories)  

---

## 🖥️ Running PenTBox on macOS & Windows

### 🛠️ macOS Setup (No Need for Kali Linux)
Since **macOS is UNIX-based**, you **do not need to install Kali Linux** to run PenTBox.

### 1️⃣ Check if Ruby is Installed
Open **Terminal** (`Command + Space`, type **Terminal**, and hit Enter).  

Run:
```bash
ruby -v

```


If Ruby is not installed, install it using:

```bash
brew install ruby

```
## 🛠️ Windows Setup (Requires Kali Linux)
Windows **does not natively support PenTBox**, so you need to install **Kali Linux** first.  

### 1️⃣ Options to Run Kali Linux on Windows  

- **Use a Virtual Machine (VM)** – Install **Kali Linux in VirtualBox/VMware**.  
- **Dual Boot** – Install **Kali alongside Windows**.  
- **Use Windows Subsystem for Linux (WSL)** – Install **Kali WSL** (limited GUI support).  

Once **Kali Linux is installed**, follow the same steps as **Linux/macOS**.


## 🚀 Installing & Running PenTBox

### 1️⃣ Clone PenTBox Repository  
Run the following command in **Terminal (macOS/Linux) or Kali Linux VM**:  

```bash
git clone https://github.com/whitehatpanda/PenTBox.git
cd PenTBox

```

2️⃣ Run PenTBox

```bash
ruby pentbox.rb

```


### 3️⃣ Select the Honeypot Tool  
- Choose **2 (Network Tools)**  
- Select **Honeypot**  
- Configure the **port** (e.g., **80 for HTTP**)  
- Start **monitoring attack logs**  

## 📊 Screenshots  
Below are some **screenshots of the implementation**: 
Step	Screenshot
Checking Ruby Version	

![image](https://github.com/user-attachments/assets/6f906aa5-055f-4f5a-98d0-6997fd3022b9)

Installing Ruby (macOS)	

![image](https://github.com/user-attachments/assets/6ade4b8c-94d9-4363-9fa0-5762bc290c3f)

Cloning PenTBox	

![image](https://github.com/user-attachments/assets/b2a40d49-4ca9-417a-8e18-0146bea67343)

Running PenTBox	

![image](https://github.com/user-attachments/assets/b3083925-f519-4450-9aff-69870568ee2d)

Honeypot Output	

![image](https://github.com/user-attachments/assets/27443203-f429-46e0-9d3a-07f497019695)

## 🚀 Implementation


1. Download the implementation folder and navigate to it.
2. Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt

   ```
### 🚀 Running the Application

3. Run the application:

   ```bash
   python app.py

    ```
4. Once the application is running, you will see a message in the terminal like:
 ```csharp
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
Open your web browser and type the IP address http://127.0.0.1:5000/ in the address bar to access the application.

- When a user loads the page, they see **only one visible input field**:  
  👉 **Name** field.

- They fill it out and submit the form.

- As long as the following conditions are met:
  - 🚫 **No hidden fields** are touched
  - 🚫 **The hidden checkbox** is left **untouched**
  - 🚫 **The hidden textbox** remains **empty**
  - ⏳ **The submission time is more than 3 seconds**

The form will be submitted successfully and shows:

> ✅ Form submitted successfully!

## Fast Submissions (Bot-like Behavior)

- If a bot submits the form **immediately after loading the page** (under 3 seconds),
- The backend detects it and **blocks the request**.

Result:

> ❌ Form blocked: Submitted too quickly

---

## 🎭 Manipulating Hidden Fields (Advanced Bot Detection)

There is an additional bot trap using **hidden fields** inside the form:

```html
<div style="display: none;">
    <label>Check me if you're a bot</label>
    <input type="checkbox" name="bot_check">

    <label>Bot textbox trap</label>
    <input type="text" name="bot_textbox">
</div>

```

Here if I change the display of both to display: block; then the fields will also be visible to us.
Previously it was hidden.

🚨 Behavior After Manipulation
If you fill these hidden fields and submit the form:

❌ Form blocked: Bot behavior detected

This mechanism helps detect bots who try to tamper with the website.

[Bots usually auto check all checkbox, So this way be can prevent bots from harming our webiste]



## 📌 Conclusion  
This project demonstrated the **implementation of a honeypot using PenTBox in Kali Linux**.  

✅ **PenTBox** provides an **easy-to-use security suite** for penetration testing.  
✅ The **honeypot tool** helps **detect, log, and analyze unauthorized access attempts**.  
✅ **Kali Linux is required for Windows**, but **macOS can run PenTBox directly**.  


#️⃣ Hashtags for SEO

#KaliLinux #PenTBox #Honeypot #CyberSecurity #EthicalHacking #InformationSecurity #NetworkSecurity #PenetrationTesting #LinuxSecurity #CyberDefense #WhiteHatHacker #SecurityTools #KaliLinuxTools #OffensiveSecurity #HackingTools #SecurityTesting #DigitalForensics #RubyProgramming #BotDetection #WebSecurity #PythonSecurity #NetworkMonitoring #ITSecurity #HoneypotDeployment #LinuxHoneypot #OpenSourceSecurity #MacOSSecurity #WindowsSecurity #CyberThreats #ThreatDetection

