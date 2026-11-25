import pygame

class Slider:
    def __init__(self, x, y, breite, hoehe, min_wert=0, max_wert=100, startwert=50):
        """
        x, y: Position der Slider-Spur (oben-links)
        breite, hoehe: Größe der Spur
        min_wert, max_wert: Wertebereich
        startwert: Anfangswert
        """
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe
        self.min_wert = min_wert
        self.max_wert = max_wert
        
        # Griff-Eigenschaften
        self.griff_radius = 8
        self.wird_gezogen = False
        
        # Wert initialisieren
        self.wert = max(min_wert, min(startwert, max_wert))
        self.griff_x = self._wert_zu_position(self.wert)
        
        # Farben
        self.farbe_spur = (100, 100, 100)
        self.farbe_griff = (200, 200, 200)
        self.farbe_griff_aktiv = (255, 255, 255)
        self.farbe_text = (255, 255, 255)
        
        # Font für Wertanzeige
        self.font = pygame.font.Font(None, 24)
    
    def _position_zu_wert(self, griff_x):
        """Konvertiert Griff-Position zu Wert"""
        # Griff-Position clampen auf die Spur
        griff_x_clamped = max(self.x, min(griff_x, self.x + self.breite))
        
        # Prozentual berechnen
        prozent = (griff_x_clamped - self.x) / self.breite
        wert = self.min_wert + prozent * (self.max_wert - self.min_wert)
        
        return int(wert)
    
    def _wert_zu_position(self, wert):
        """Konvertiert Wert zu Griff-Position"""
        prozent = (wert - self.min_wert) / (self.max_wert - self.min_wert)
        griff_x = self.x + prozent * self.breite
        
        return griff_x
    
    def handle_event(self, event):
        """Verarbeitet Maus-Events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mausklick prüfen
            mouse_x, mouse_y = event.pos
            
            # Ist der Griff geklickt?
            if self._griff_getroffen(mouse_x, mouse_y):
                self.wird_gezogen = True
            # Oder wurde auf die Spur geklickt?
            elif self._spur_getroffen(mouse_x, mouse_y):
                self.griff_x = mouse_x
                self.wert = self._position_zu_wert(mouse_x)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.wird_gezogen = False
        
        elif event.type == pygame.MOUSEMOTION and self.wird_gezogen:
            # Griff ziehen
            mouse_x, mouse_y = event.pos
            self.griff_x = mouse_x
            self.wert = self._position_zu_wert(mouse_x)
    
    def _griff_getroffen(self, mouse_x, mouse_y):
        """Prüft, ob Maus auf dem Griff ist"""
        abstand_x = abs(mouse_x - self.griff_x)
        abstand_y = abs(mouse_y - (self.y + self.hoehe // 2))
        
        return abstand_x <= self.griff_radius + 5 and abstand_y <= self.griff_radius + 5
    
    def _spur_getroffen(self, mouse_x, mouse_y):
        """Prüft, ob Maus auf der Spur ist"""
        return (self.x <= mouse_x <= self.x + self.breite and 
                self.y <= mouse_y <= self.y + self.hoehe)
    
    def draw(self, screen):
        """Zeichnet den Slider"""
        # Spur zeichnen
        spur_rect = pygame.Rect(self.x, self.y + self.hoehe // 2 - 3, self.breite, 6)
        pygame.draw.rect(screen, self.farbe_spur, spur_rect)
        
        # Griff zeichnen
        farbe = self.farbe_griff_aktiv if self.wird_gezogen else self.farbe_griff
        pygame.draw.circle(screen, farbe, (int(self.griff_x), self.y + self.hoehe // 2), self.griff_radius)
        
        # Wertanzeige zeichnen
        wert_text = self.font.render(f"{self.wert}%", True, self.farbe_text)
        text_x = self.x + self.breite + 15
        text_y = self.y + self.hoehe // 2 - wert_text.get_height() // 2
        screen.blit(wert_text, (text_x, text_y))
    
    def get_value(self):
        """Gibt den aktuellen Wert zurück (0-100)"""
        return self.wert
    
    def set_value(self, wert):
        """Setzt einen neuen Wert"""
        self.wert = max(self.min_wert, min(wert, self.max_wert))
        self.griff_x = self._wert_zu_position(self.wert)
