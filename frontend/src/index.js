import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import Lottie from 'react-lottie';
import * as homeAnimationData from './resources/home.json';

const HelloWorld = () => {
  const [isStopped, setIsStopped] = useState(false);

  const defaultOptions = {
    loop: false,
    autoplay: true,
    animationData: homeAnimationData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  };

  const handleClick = () => {
    setIsStopped(false);
  };

  return (
    <div>
      <h1>Hello World!</h1>
      <Lottie
        options={defaultOptions}
        height={400}
        width={400}
        isStopped={isStopped}
        eventListeners={[
          {
            eventName: 'complete',
            callback: () => setIsStopped(true),
          },
        ]}
        onClick={handleClick}
      />
    </div>
  );
};

ReactDOM.render(<HelloWorld />, document.getElementById('root'));