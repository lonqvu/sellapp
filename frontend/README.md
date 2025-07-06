# Vue 3 Base Project (Vite + TypeScript)

## Tính năng tích hợp
- Vue 3 + Vite + TypeScript
- Pinia (state management)
- Vue Router
- Axios
- Element Plus UI
- ESLint + Prettier
- Vitest (unit test)
- Husky, lint-staged, Commitlint
- TailwindCSS (nếu muốn dùng thêm)

## Cấu trúc thư mục
```
frontend/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   │   └── common/
│   ├── composables/
│   ├── constants/
│   ├── directives/
│   ├── layouts/
│   ├── pages/
│   ├── router/
│   ├── services/
│   ├── stores/
│   └── utils/
├── tests/
│   └── unit/
├── .env, .env.development, .env.production
├── .eslintrc.js, .prettierrc, .gitignore
├── README.md
├── tsconfig.json
├── vite.config.ts
├── package.json
```

## Cài đặt & phát triển
```bash
npm install
npm run dev
```

## Kiểm tra code & format
```bash
npm run lint
npm run format
```

## Unit test
```bash
npm run test:unit
```

## Commit chuẩn convention
```bash
npm run commit
```

## Build production
```bash
npm run build
```
