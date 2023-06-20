# SafyPay

## Project Description

This project, SafyPay, was developed as a submission for the [Diversion Hackathon](https://diversion.tech).

SafyPay is a Django-based platform designed to address the trust and security challenges faced by online transactions and e-commerce, with a particular focus on small businesses and high-value goods. Our platform offers an escrow service and dispute resolution process, backed by a trusted third-party delivery partner, to provide a secure and trustworthy transaction experience for both buyers and sellers.

SafyPay aims to solve the problem of fraudulent orders and payment disputes, which can be a significant concern for small businesses. By implementing an escrow service, funds are securely held until both parties agree that the transaction has been successfully completed. This approach helps prevent fraud and reduces the risk of payment disputes.

Additionally, our platform provides a marketplace where buyers can make purchases with confidence, knowing they will receive authentic and as-advertised products.

Our mission is to empower small businesses to sell their products with confidence, while providing buyers a secure and transparent platform for online purchases. We are committed to building trust and transparency in the realm of online commerce, benefiting all participants.

## Key Features

- Escrow service for secure transactions
- Dispute resolution process for fair resolutions
- Trusted third-party delivery partner
- Fraud prevention and risk reduction
- Marketplace for trusted purchases

## Installation

To run SafyPay locally, follow these steps:

1. Clone the repository:

```
shell
git clone https://github.com/your-username/safypay.git
```

2. Install the necessary dependencies:
```
cd safypay
pip install -r requirements.txt
```

3. Configure the environment variables:
```
cp .env.example .env
Edit the .env file and provide the required configuration values.
```

4. Run database migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```
6. Open your browser and navigate to http://localhost:8000 to access SafyPay.


## Contributing
We welcome contributions from the community! If you'd like to contribute to SafyPay, please follow these guidelines:

1. Fork the repository and create your branch:

2. Commit your changes and push to your forked repository

3. Open a pull request, describing your changes and why they should be merged.

## License

This project is licensed under the [MIT License](LICENSE).
