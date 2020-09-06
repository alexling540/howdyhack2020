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
              text='Identify suspicious individuals'
              label='Facial Recognition'
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
