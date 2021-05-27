FROM node:12

WORKDIR /usr/src/app

COPY package.json ./

RUN npm install -g npm@6.14.6
RUN npm install
RUN npm install @material-ui/lab --save

COPY ./ ./

EXPOSE 3000
CMD ["npm", "run", "start"]