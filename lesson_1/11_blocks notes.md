## Understanding the Problem

- input: integer representing the number of blocks available
- output: integer representing the number of leftover blocks after building the tallest possible valid structure

# rules
- explicit: 
  - The blocks are all cubes
  - The structure is built in layers
  - The top layer is a single block
  - Each block in an upper layer must be supported by 4 blocks in the layer below it. 
  - Each block in a lower layer *can* support more than 1 block above it. 
  - You cannot leave gaps between the blocks. 

- implicit:
  - When calculating your structure, you will start with the top layer and work down
  - The layer number is the same as the number of blocks one one side of that layer; so the total blocks in a layer is the layer number squared.
  
- Questions:
  - I'm picturing a square pyramid, but maybe I need to question that assumption... could each upper block be supported by more than 4 lower blocks? >>> After looking at test cases, it should be a square pyramid. So my implicit assumptions were correct.

## Data Structures
- We're working with integers to start.
- We will do some calculating of the number of blocks in each layer, incrementing as we do so, and adding. 
- If we will need to store the number of items in each layer, I think a nested list is a good idea, since we don't know how many layers we may need to calculate.

## Algorithm
# First Draft
- 1. start with layer 1 which has 1 block
- 2. calculate how many blocks are in each consecutive layer
- 3. sum up the total of all the blocks in all the layers so far 
- 4. Repeat steps 1-3 until that sum total is equal to or greater than the number of available blocks
- 5. Remove the number of blocks from the last layer you attempted to build, so your total is now just of the layers you successfully built
- 6. Take your number of available blocks and subtract the total you built in your structure. 
- 7. Return that difference.

# Experiment w/ improving this one ^ (it will be clunkier)
- 1. Set:
  - "blocks used so far" is set to 0
  - "layer" starts at 0
  - "blocks in this layer" starts at 0
- 3. Begin repeating process:
  - Check if "blocks used so far" is greater than or equal to the input number.
    -If not:
      - Add "blocks in this layer" to "blocks used so far"
      - increment "layer" by 1
      - Calculate new "blocks in this layer" by squaring layer number
    -If so:
      - Subtract "blocks in this layer" from "blocks used so far"
      - Subtract "blocks used so far" from the input number and return the difference.


# Second draft
- 1. Starting numbers:
  - "Available blocks" is set to the input number
  - "Layer" is set to 0
  - "Blocks in this layer" is set to 0
- 2. Begin repeating process:
  - Subtract "blocks in this layer" from "available blocks"
  - Increment "layer" by 1
  - Calculate new "blocks in this layer" by squaring layer number
- 3. Break the loop of #2, when "blocks in this layer" is greater than "available blocks" (at that point do not complete step 2 again)
- 4. Return "available blocks"