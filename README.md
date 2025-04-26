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



## 📌 Conclusion  
This project demonstrated the **implementation of a honeypot using PenTBox in Kali Linux**.  

✅ **PenTBox** provides an **easy-to-use security suite** for penetration testing.  
✅ The **honeypot tool** helps **detect, log, and analyze unauthorized access attempts**.  
✅ **Kali Linux is required for Windows**, but **macOS can run PenTBox directly**.  



