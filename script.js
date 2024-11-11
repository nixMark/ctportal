// Array of file objects with name and path (update with your file paths)
const files = [
  { name: "Clearance", path: "contents/documents/clearance.pdf" },
  { name: "Expedition Photo 01", path: "contents/images/expedition01.png" },
  { name: "Report", path: "contents/documents/docs1.pdf" },
  { name: "Report on Mystery Man", path: "contents/documents/mysteryMan.pdf" },
  { name: "Pocket Map", path: "contents/images/pocketMap.png"},
  { name: "Recommendation from Karl Ernst Rash", path: "contents/documents/Recommendation - Karl Ernst Rasch.pdf" },
  { name: "Expedition Photo 02", path: "contents/images/expedition02.png" },
  { name: "Recommendation from Nathan Gould", path: "contents/documents/Recommendation - Nathan Gould.pdf" },
  { name: "Report on Kanan Hasanli", path: "contents/documents/reportKH.pdf" },
  { name: "Invitation Note", path: "contents/images/invitation.png"},
  ];
  
  // Populate sidebar with file names
  const fileList = document.getElementById("file-list");
  files.forEach((file, index) => {
    const listItem = document.createElement("li");
    listItem.textContent = file.name;
    listItem.onclick = () => viewFile(file.path);
    fileList.appendChild(listItem);
  });
  
  // Function to display selected file
  function viewFile(path) {
    const viewer = document.getElementById("viewer");
    viewer.innerHTML = ""; // Clear viewer
  
    if (path.endsWith(".pdf")) {
      // Display PDF
      const iframe = document.createElement("iframe");
      iframe.src = path;
      iframe.width = "100%";
      iframe.height = "100%";
      viewer.appendChild(iframe);
    } else if (path.match(/\.(jpg|jpeg|png|gif)$/)) {
      // Display Image
      const img = document.createElement("img");
      img.src = path;
      viewer.appendChild(img);
    }
  }