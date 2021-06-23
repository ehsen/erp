class DebitCreditNotEqual(Exception):
    pass

class DocIDFailed(Exception):
    """
    This exception will be raised when ERP fails to generate doc_id for a document. For example
    doc_id for trasnaction, account or something like that. Its a critical error.

    HOW TO DEAL WITH THIS EXCEPTION:
    ---------------------------------

    Most likely there is something wrong with database connection. Fix the connection and error will
    be gone.
    """
    pass