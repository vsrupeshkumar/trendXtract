import React from 'react';
import './index.css';

function App() {
  const scrollToHistory = () => {
    const history = document.getElementById('history');
    if (history) history.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <div className="w-full h-full bg-white dark:bg-gray-100 dark:text-gray-800">
      {/* Top Hero Section */}
      <section className="container flex flex-col mx-auto lg:flex-row">
        {/* Left image block */}
        <div
          className="w-full lg:w-1/3"
          style={{
            backgroundImage: "url('https://source.unsplash.com/random/640x480')",
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            minHeight: '400px',
          }}
        ></div>

        {/* Right content block */}
        <div className="flex flex-col w-full p-6 lg:w-2/3 md:p-8 lg:p-12 relative">
          <h1 className="text-4xl font-bold mb-4 text-violet-600">trendXtract</h1>
          <p className="text-xl mb-6">Explore research publications</p>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            className="w-8 h-8 mb-8 text-violet-600"
          >
            <path
              fillRule="evenodd"
              d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>

          {/* Scroll Down Button */}
          <button
            onClick={scrollToHistory}
            className="fixed right-6 bottom-6 bg-violet-600 hover:bg-violet-700 text-white px-4 py-3 rounded-full shadow-lg transition"
          >
            ↓
          </button>
        </div>
      </section>

      {/* Dashboard Section */}
      <section
        id="history"
        className="w-full p-10 mt-20 bg-white dark:bg-gray-200 text-gray-800"
      >
        <h2 className="text-3xl font-bold mb-4">📊 History Dashboard</h2>
        <p className="text-gray-600 mb-4">
          You will see all your AI trend searches here in the future.
        </p>
        <div className="border-t border-gray-300 pt-4">
          <ul className="list-disc ml-5">
            <li>Example Topic 1: Generative AI (searched 3 times)</li>
            <li>Example Topic 2: AI Agents (searched 1 time)</li>
          </ul>
        </div>
      </section>
    </div>
  );
}

export default App;
