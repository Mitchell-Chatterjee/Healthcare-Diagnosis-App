# Security Configuration Guide

This document provides guidance on securely configuring the healthcare agents for public deployment.

## 🔐 Environment Variables

To use this healthcare package safely in production, configure the following environment variables:

### Required API Keys

```bash
# Azure OpenAI (for evaluation models)
export AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
export AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com"

# Google Search (for research agent)
export GOOGLE_API_KEY="your-google-api-key"
export GOOGLE_CSE_ID="your-custom-search-engine-id"

# DeepEval (for evaluation metrics)
export DEEPEVAL_API_KEY="your-deepeval-api-key"
```

### Optional Model Configuration

```bash
# Mistral API (if using Mistral models)
export MISTRAL_API_KEY="your-mistral-api-key"

# OpenAI API (alternative model provider)
export OPENAI_API_KEY="your-openai-api-key"

# Anthropic API (alternative model provider)
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

## 🔒 Security Best Practices

### 1. Environment-Based Configuration

Never hardcode API keys or sensitive information in source code. Use environment variables:

```python
import os

# ✅ Good - Use environment variables
api_key = os.getenv("AZURE_OPENAI_API_KEY")

# ❌ Bad - Hardcoded API key
api_key = "65d029290f3e45d2b4422eba1138e148"
```

### 2. Configuration Files

Create a `.env` file for local development (never commit this file):

```bash
# .env file (add to .gitignore)
AZURE_OPENAI_API_KEY=your-actual-key-here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com
GOOGLE_API_KEY=your-google-key-here
```

### 3. Production Deployment

For production deployments:

- Use secure secret management services (AWS Secrets Manager, Azure Key Vault, etc.)
- Rotate API keys regularly
- Use least-privilege access principles
- Monitor API usage and set up alerts for unusual activity

### 4. Database Security

The healthcare agents create local SQLite databases for storage:

- In production, use encrypted databases
- Consider using cloud-managed database services
- Implement proper backup and recovery procedures
- Ensure databases are not accessible publicly

## 🛡️ Files to Exclude from Version Control

Ensure your `.gitignore` includes:

```gitignore
# API Keys and Secrets
*.env
.env.*
**/api_keys/
**/.deepeval/.deepeval

# Database files
*.db
*.sqlite
*.sqlite3

# Temporary files
*.tmp
*.temp
.tmp/
temp/

# Logs
*.log
logs/
```

## 🔍 Security Checklist

Before making the repository public:

- [ ] No API keys or secrets in source code
- [ ] All `.deepeval` API key files removed
- [ ] Proper `.gitignore` files in place
- [ ] Environment variable usage documented
- [ ] Test configurations use placeholder values
- [ ] Database files excluded from version control
- [ ] Sensitive logs excluded from version control

## 📞 Support

If you need help with secure configuration, please refer to:

- [Agno Framework Security Documentation](https://docs.agno.ai/security)
- [Azure OpenAI Best Practices](https://docs.microsoft.com/azure/cognitive-services/openai/concepts/security)
- [Google API Security](https://developers.google.com/apis/docs/security)

## ⚠️ Important Notes

1. **Never commit real API keys** to version control
2. **Rotate compromised keys immediately** if accidentally exposed
3. **Monitor API usage** for unauthorized access
4. **Use separate keys** for development, testing, and production environments
5. **Review access logs regularly** for security incidents
