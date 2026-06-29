# Install and Configure Splunk

## Objective
To install and configure Splunk Enterprise for collecting, indexing, and analyzing machine-generated data for monitoring and security analysis.

## Steps to Install and Configure Splunk on Ubuntu

## Step 1: Download Splunk

1. Open the terminal and download Splunk using `wget`:

```bash
wget -O splunk-9.3.0-51ccf43db5bd-linux-2.6-amd64.deb "https://download.splunk.com/products/splunk/releases/9.3.0/linux/splunk-9.3.0-51ccf43db5bd-linux-2.6-amd64.deb"
```

2. Once the download is complete, install Splunk:

```bash
sudo dpkg -i splunk-ubuntu.deb
```

---

## Step 2: Enable Splunk as a Service

1. Move to the Splunk installation directory:

```bash
cd /opt/splunk/bin
```

2. Accept the license agreement and enable Splunk to start automatically at boot:

```bash
sudo ./splunk enable boot-start --accept-license
```

3. Start the Splunk service:

```bash
sudo ./splunk start
```

4. When prompted, create an **admin username** and **password**.

---

## Step 3: Access the Splunk Web Interface

1. Open your web browser and navigate to:

```text
http://<your-server-ip>:8000
```

2. Log in using the administrator credentials you created during setup.

---

# Conclusion

- ✅ Successfully installed Splunk Enterprise on Ubuntu.
- ✅ Configured Splunk to start automatically as a system service.
- ✅ Accessed the Splunk Web Interface using port **8000**.
- ✅ Ready to ingest, search, and analyze log data.