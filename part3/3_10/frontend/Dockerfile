FROM node:16-alpine
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./ 
RUN npm install

COPY . .

EXPOSE 3002

ENV PORT 3002

CMD ["npm", "run", "dev"]