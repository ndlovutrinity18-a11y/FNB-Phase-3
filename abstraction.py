class EmailService:
    def _connect_to_email_server(self):
        """Simulate connecting to an email server."""
        print("Connecting to email server...") 
        
    def _authenticate_user(self):
        print(f"Authenticating user:")
        # Simulate successful authentication
        return True

    def send_email(self):
        """Send an email."""
        self._connect_to_email_server()
        self._authenticate_user
        print("Sending email...") 
        self.disconnect
        
    def disconnect(self):
        """Simulate disconnecting from the email server."""                
        print("Disconnecting from email server...")
email = EmailService()
email.send_email()