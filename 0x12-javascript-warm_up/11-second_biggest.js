#!/usr/bin/node
const nums = process.argv;

if (nums.length <= 3) {
  console.log(0);
} else {
  const sortedNums = nums.slice(2).sort((a, b) => a - b);
  console.log(sortedNums[sortedNums.length - 2]);
}
