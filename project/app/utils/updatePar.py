def updateParameters(object, data):
    object.title = data.title
    object.genre = data.genre
    object.creator = data.creator
    return object

def updateReview(object, data):
    object.text = data.text
    object.rating = data.rating
    return object