from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def working_test(request):
    """Completely isolated test with no redirects whatsoever"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>WORKING TEST</title>
        <style>body { font-family: Arial; margin: 50px; }</style>
    </head>
    <body>
        <h1 style="color: green;">✅ THIS IS WORKING!</h1>
        <p><strong>No redirects here!</strong></p>
        <p>User: {}</p>
        <p>Authenticated: {}</p>
        <p>Session Key: {}</p>
        <hr>
        <p>If you see this, the server is working fine.</p>
        <p>The issue is specifically with the main dashboard URL.</p>
        <a href="/dashboard/">Try Dashboard</a> |
        <a href="/login/">Login</a>
    </body>
    </html>
    """.format(
        str(request.user), 
        request.user.is_authenticated,
        request.session.session_key
    ))

def dashboard_home(request):
    print("DEBUG: Dashboard view called!")
    print(f"DEBUG: User: {request.user}")
    print(f"DEBUG: Is authenticated: {request.user.is_authenticated}")
    print(f"DEBUG: Request method: {request.method}")
    print(f"DEBUG: Request path: {request.path}")
    
    # Manual authentication check to avoid redirect loop
    if not request.user.is_authenticated:
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head><title>Login Required</title></head>
        <body>
            <h1>Login Required</h1>
            <p>You need to login to access the dashboard.</p>
            <a href="/login/">Go to Login</a>
        </body>
        </html>
        """)
    
    # Dashboard for authenticated users
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - SUCCESS!</title>
        <style>
            body {{ font-family: Arial; margin: 50px; }}
            .success {{ color: green; font-size: 24px; }}
            .info {{ background: #e7f3ff; padding: 15px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1 class="success">🎉 Dashboard is Working!</h1>
        <div class="info">
            <p><strong>✅ SUCCESS!</strong> You are successfully logged in and viewing the dashboard.</p>
            <p><strong>User:</strong> {}</p>
            <p><strong>Email:</strong> {}</p>
            <p><strong>Authenticated:</strong> {}</p>
            <p><strong>Path:</strong> {}</p>
            <p><strong>User ID:</strong> {}</p>
        </div>
        <hr>
        <a href="/logout/" style="color: red;">Logout</a> | 
        <a href="/" style="color: blue;">Home</a> |
        <a href="/dashboard/test/" style="color: green;">Test Page</a>
    </body>
    </html>
    """.format(
        request.user.first_name or "No name", 
        getattr(request.user, 'email', 'No email'),
        request.user.is_authenticated,
        request.path,
        request.user.id if request.user.is_authenticated else "N/A"
    ))

def test_view(request):
    """Ultra simple test view"""
    return HttpResponse("<h1>TEST PAGE WORKS!</h1><p>If you see this, the routing is working.</p><a href='/dashboard/'>Back to Dashboard</a>")

def simple_dashboard(request):
    """Simple dashboard without login required for testing"""
    return HttpResponse("""
    <h1>🎉 SIMPLE DASHBOARD TEST</h1>
    <p>This is a dashboard without login required.</p>
    <p>User: {}</p>
    <p>Authenticated: {}</p>
    <a href='/login/'>Go to Login</a> | 
    <a href='/dashboard/'>Go to Real Dashboard</a>
    """.format(request.user, request.user.is_authenticated))