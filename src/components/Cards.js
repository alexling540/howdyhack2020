import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Check out these EPIC Tools!</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/img-9.jpg'
              text='Use image detection to comb the internet for a match of a person'
              label='Find a Certain Person'
              path='/face_rec'
            />
            <CardItem
              src='images/img-2.jpg'
              text='Put on a disguise to traverse public areas unnoticed'
              label='Disguise Yourself'
              path='/disguise'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
