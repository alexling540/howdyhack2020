import React from 'react';
import '../../App.css';
import Footer from '../Footer';

export default function face_rec() {

  return (
    <>
      <h1 className='disguise'>DISGUISE</h1>;

      <div className='par__container'>
        <form method='post' enctype='multipart/form-data'>
          <p>
            <input type='file' class='btn--medium' name='file'/>
            <br />
            <input type="radio" id="choice1" name="option" value="regular" />
            <label for="choice1">
              Regular Glasses
        </label>
            <br />
            <input type="radio" id="choice2" name="option" value="deal" />
            <label for="choice2">
              "Deal with it" Sunglasses
        </label>
            <br />
            <br />
            <input type='submit' class='btn--medium' value='Upload' />
          </p>
        </form>


      </div>

      <Footer />
    </>
  );
}
