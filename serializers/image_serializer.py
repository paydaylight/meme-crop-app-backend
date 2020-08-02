from flask import jsonify,request


def serialize_image(img):
    return jsonify(id=img.id,
                   caption=img.caption,
                   url=f"{request.url_root}{img.url}",
                   finished=img.finished,
                   created_at=img.created_at)