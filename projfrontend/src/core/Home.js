import React, { useEffect, useState } from "react";
import { getProducts } from "./helper/coreapicalls";
export const Home = () => {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
      loadAllProducts();
  }, []);
  const loadAllProducts = () => {
    getProducts()
      .then((data) => {
        if (data.error) {
          setError(data.error);
        } else {
        console.log(data);
          setProducts(data);
        }
      })
      .catch((err) => console.log(err));
  };
  return (
    <div>
      <h1>Home Component</h1>
      <div className="row">
          {products.map((product,index)=>{
              return(
              <h1 key={index}>{product.name}</h1>
              )
          })}
      </div>
    </div>
  );
};
