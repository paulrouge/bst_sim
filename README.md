# bst simulation model

_BST is a version of a so called "up only" contract. Each swap is taxed, the taxed value stays in the protocol, thus making it so that the price goes "up only". 

This might sound pretty ponzi, but keep in mind that the incoming value is coming from the Blobble game. All the bnusd spend within the game is going through the BST contract. We will also use our node reward to mint BST using bnUSD. And distriubte that BST to healthy Blobble owners._

## How to run

main.py is the entry of the program. It's all a bit wonky because this is just a sketch to get a proof of concept working. There might be some redundant code/logic here and there.

In main.py there is a "main loop" that runs the simulation. To simulate real txs / behavior, I tried to introduce randomness for each mint or redeem tx.

In `root/config.py` you can set the parameters for the simulation. CHUNK_SIZE is the size of chunks in bnusd value. It was introduced to see if there is a change in price when whale transactions are split into smaller chunks. 

example:

    with a chunksize of 500, a tx worth 1600 bnusd will be split into 3 chunks of 500 bnusd each, and a remainer of 100. Each chunk, and the remaining 100, is taxed, and the new price is calculated based on the new supply.

So after you checked and set the config.py you can run the simulation with:

```bash
    python3 main.py
```

