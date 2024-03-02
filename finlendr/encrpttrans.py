from cryptography.fernet import Fernet

 
def generate_encryption_key():
    return Fernet.generate_key()


def encrypt_transaction_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data


def decrypt_transaction_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    encrypted_amount = db.Column(db.String(255), nullable=False)
    encrypted_details = db.Column(db.String(255), nullable=True)
    # Add more fields as needed


@app.route('/transaction', methods=['POST'])
def create_transaction():
    sender_id = request.json.get('sender_id')
    receiver_id = request.json.get('receiver_id')
    amount = request.json.get('amount')
    details = request.json.get('details')
    

    key = generate_encryption_key()
    encrypted_amount = encrypt_transaction_data(amount, key)
    encrypted_details = encrypt_transaction_data(details, key) if details else None
    
    new_transaction = Transaction(sender_id=sender_id, receiver_id=receiver_id,
                                  encrypted_amount=encrypted_amount, encrypted_details=encrypted_details)
    db.session.add(new_transaction)
    db.session.commit()
    
    return jsonify({'message': 'Transaction created successfully'}), 201


@app.route('/transaction/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'error': 'Transaction not found'}), 404
    

    key = get_encryption_key_for_transaction(transaction)
    amount = decrypt_transaction_data(transaction.encrypted_amount, key)
    details = decrypt_transaction_data(transaction.encrypted_details, key) if transaction.encrypted_details else None
    
    return jsonify({
        'id': transaction.id,
        'sender_id': transaction.sender_id,
        'receiver_id': transaction.receiver_id,
        'amount': amount,
        'details': details
    }), 200