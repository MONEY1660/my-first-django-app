# my-first-django-app

## GitHub and Vercel Deployment

1. Initialize git and add remote repository:

```bash
git init
git add .
git commit -m "Initial Django project"
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

2. Connect repository to Vercel:
   - เข้า Vercel dashboard
   - เลือก Import Project -> จาก GitHub
   - เลือก repository นี้ แล้วกด Deploy

3. ตั้ง environment variables ใน Vercel:
   - `DJANGO_SECRET_KEY` = ค่าลับของคุณ
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_ALLOWED_HOSTS` = `*` หรือชื่อโดเมนของคุณ
   - `DATABASE_URL` = หากใช้ฐานข้อมูลภายนอก

4. หากต้องการใช้ SQLite ทุกอย่างพร้อม deploy แล้ว แต่ควรใช้ฐานข้อมูลภายนอกใน production.
