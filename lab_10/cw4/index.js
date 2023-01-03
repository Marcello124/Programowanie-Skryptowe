import Operation from './module.mjs';

const operacja = new Operation(Number(process.argv[2]), Number(process.argv[3]));
operacja.show();