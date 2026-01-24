# Zero-Cost Deployment Guide (Render + Neon.tech)

This guide helps you deploy the app for FREE without needing a credit card.

## Strategy
- **Web App**: Hosting on **Render Free Tier**.
- **Database**: Hosting on **Neon.tech Free Tier** (PostgreSQL).

---

## Step 1: Create Free Database (Neon.tech)
1. Go to [Neon.tech](https://neon.tech) and Sign Up (GitHub/Google).
2. Click **Create Project**.
3. **Name**: `dsa-contest-db`.
4. **Region**: Choose one close to you (e.g., Singapore).
5. Copy the **Connection String** (Postgres URL).
   - It looks like: `postgres://neondb_owner:AbCd123@ep-cool-frog-123456.ap-southeast-1.aws.neon.tech/neondb?sslmode=require`

## Step 2: Deploy Web Service (Render)
1. Go to [Render Dashboard](https://dashboard.render.com).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. **Name**: `dsa-challenge-app`.
5. **Runtime**: Select **Docker**. (CRITICAL: Select Docker, not Python).
6. **Instance Type**: Select **Free**.
7. **Environment Variables**:
   Add the following variables:
   - `DATABASE_URL`: Paste the **Connection String** from Neon.tech (Step 1).
   - `SECRET_KEY`: `any-random-string-here`
   - `WEB_CONCURRENCY`: `1` (CRITICAL: Limits workers to save RAM).
   - `PYTHONUNBUFFERED`: `true`

## Step 3: Important Usage Instructions
> [!WARNING]
> **Free Tier Limitations**
> 1.  **Spin Down**: If no one uses the site for 15 minutes, it "sleeps". The first person to visit will wait ~1 minute for it to wake up. **Keep the site open 10 minutes before the contest starts.**
> 2.  **Concurrency**: We have limited the server to "1 Worker" to prevent crashing. **Instruct students to NOT click "Run" all at the exact same second.**

### Troubleshooting
- **Database Errors**: Ensure you copied the full Neon URL.
- **Build Failed**: Check logs. If "Out of Memory", we might need to reduce Java memory settings further in `executor.py`.
