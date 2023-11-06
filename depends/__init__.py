from fastapi import Header,Request

def sample_depends(
    sontenttype = Header(...),
    request: Request = None
):
    print(content_type, request)