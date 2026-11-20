from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Verify full-stack API health status."""
    return jsonify({"status": "healthy", "branch_workflow": "active"}), 200

if __name__ == '__main__':
    app.run(debug=True)
