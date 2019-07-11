# coding: utf-8

"""
    Avaza API Documentation

    Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "avazacli"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Avaza API Documentation",
    author_email="",
    url="",
    keywords=["Swagger", "Avaza API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Welcome to the autogenerated documentation &amp; test tool for Avaza&#39;s API. &lt;br/&gt;&lt;br/&gt;&lt;strong&gt;API Security &amp; Authentication&lt;/strong&gt;&lt;br/&gt;Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS &lt;br/&gt;&lt;br/&gt;You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).&lt;br/&gt;&lt;br/&gt; OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  &lt;br/&gt;OAuth2 Token endpoint: https://any.avaza.com/oauth2/token&lt;br/&gt;Base URL for subsequent API Requests: https://api.avaza.com/ &lt;br/&gt;&lt;br/&gt;Blogpost about authenticating with Avaza&#39;s API:  https://www.avaza.com/avaza-api-oauth2-authentication/ &lt;br/&gt;Blogpost on using Avaza&#39;s webhooks: https://www.avaza.com/avaza-api-webhook-notifications/&lt;br/&gt;The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days&lt;br/&gt;The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. &lt;br/&gt;&lt;br&gt;&lt;strong&gt;Support&lt;/strong&gt;&lt;br/&gt;For API Support, and to request access please contact Avaza Support Team via our support chat. &lt;br/&gt;&lt;br/&gt;&lt;strong&gt;User Contributed Libraries:&lt;/strong&gt;&lt;br/&gt;Graciously contributed by 3rd party users like you. &lt;br/&gt;Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.&lt;br/&gt; &lt;ul&gt;&lt;li&gt; - &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;https://packagist.org/packages/debiprasad/oauth2-avaza&#39;&gt;PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;  # noqa: E501
    """
)