FROM node:12

WORKDIR /usr/src/app

COPY package.json ./

RUN npm install -g npm@6.14.6
RUN npm install

COPY ./ ./

CMD ["PORT=8000", "npm", "run", "start"]