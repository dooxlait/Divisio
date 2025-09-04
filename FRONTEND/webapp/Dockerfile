FROM node:20-alpine

WORKDIR /app

# Copier les fichiers de dépendances
COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./

# Installer les dépendances
RUN npm install --frozen-lockfile || yarn install || pnpm install

# Copier le code
COPY . .

# Exposer le port Next.js
EXPOSE 3000

# Démarrer Next.js en mode dev avec Turbopack
CMD ["npm", "run", "dev"]
