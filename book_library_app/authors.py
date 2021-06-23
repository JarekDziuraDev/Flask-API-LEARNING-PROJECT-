from flask import jsonify
from book_library_app import app
from book_library_app.model import Author, AuthorSchema


@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    #print(authors)
    return jsonify({
        'success': True,
        'data': author_schema.dump(authors)
    })


@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Get single author with id {author_id}'
    })


@app.route('/api/v1/authors', methods=['POST'])
def create_author():
    return jsonify({
        'success': True,
        'data': 'New author has been created'
    }), 201

@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_authora(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been updated'
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Author with id {author_id} has been deleted'
    })